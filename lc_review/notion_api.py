"""Direct Notion REST access for the review databases.

The MCP connection this project used before is bound to an interactive
claude.ai login, so it cannot be driven from a script. This module talks to
the REST API with an internal integration token instead, which is what makes
a batch sync possible at all.

Reads ``NOTION_TOKEN`` from the repository ``.env``.
"""

from __future__ import annotations

import os
import time
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent.parent
ENV_PATH = REPO / ".env"

API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

REVIEW_DB = "7b103d6a-78eb-4dcb-9167-f038237e6ce7"      # LC 旧题回顾
ELEMENTS_DB = "660316d4-125b-43e2-b5cc-7189d99815c7"    # LC 要素表


def load_env() -> dict[str, str]:
    """Parse the repo .env. It is gitignored; nothing here belongs in git."""
    env: dict[str, str] = {}
    if not ENV_PATH.exists():
        return env
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith(("#", ";")) or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def _token() -> str:
    token = os.environ.get("NOTION_TOKEN") or load_env().get("NOTION_TOKEN")
    if not token:
        raise RuntimeError(
            "NOTION_TOKEN not set. Create an internal integration, share the "
            "databases with it, and put the secret in .env."
        )
    return token


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_token()}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, **kwargs) -> dict:
    """One API call, retrying the rate-limit and transient-server cases.

    Notion answers 429 with a Retry-After; honouring it is the difference
    between a sync that finishes and one that dies a third of the way in.
    """
    url = f"{API}{path}"
    for attempt in range(6):
        response = requests.request(method, url, headers=_headers(), timeout=30, **kwargs)
        if response.status_code == 429:
            time.sleep(float(response.headers.get("Retry-After", 1)))
            continue
        if response.status_code >= 500:
            time.sleep(2 ** attempt)
            continue
        if response.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {response.status_code}: {response.text[:300]}")
        return response.json()
    raise RuntimeError(f"{method} {path} kept failing after retries")


def query_all(database_id: str) -> list[dict]:
    """Every row in a database, following pagination to the end."""
    rows: list[dict] = []
    cursor = None
    while True:
        payload: dict = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        data = _request("POST", f"/databases/{database_id}/query", json=payload)
        rows.extend(data.get("results", []))
        if not data.get("has_more"):
            return rows
        cursor = data["next_cursor"]


def update_page(page_id: str, properties: dict) -> dict:
    return _request("PATCH", f"/pages/{page_id}", json={"properties": properties})


def create_page(database_id: str, properties: dict) -> dict:
    return _request(
        "POST", "/pages", json={"parent": {"database_id": database_id}, "properties": properties}
    )


def append_blocks(page_id: str, blocks: list[dict]) -> dict:
    """Notion caps a children append at 100 blocks, so send it in chunks."""
    result: dict = {}
    for start in range(0, len(blocks), 100):
        result = _request(
            "PATCH", f"/blocks/{page_id}/children", json={"children": blocks[start:start + 100]}
        )
    return result


# --- property helpers -------------------------------------------------------
# Notion's property payloads are verbose and easy to get subtly wrong; these
# keep the call sites readable.

def prop_title(text: str) -> dict:
    return {"title": [{"type": "text", "text": {"content": text[:2000]}}]}


def prop_text(text: str) -> dict:
    """Rich text caps at 2000 characters per chunk, so split long bodies."""
    chunks = [text[i:i + 2000] for i in range(0, len(text), 2000)] or [""]
    return {"rich_text": [{"type": "text", "text": {"content": c}} for c in chunks]}


def prop_rich(segments: list[tuple[str, bool]]) -> dict:
    """Rich text from (text, highlighted) pairs, keeping the orange marking.

    The colour is not decoration: it is echo's own record of where she went
    wrong. Flattening it to plain text would drop that signal, so highlighted
    runs are re-emitted with Notion's orange colour and bold.
    """
    runs: list[dict] = []
    for text, highlighted in segments:
        if not text:
            continue
        for start in range(0, len(text), 2000):
            chunk = text[start:start + 2000]
            run: dict = {"type": "text", "text": {"content": chunk}}
            if highlighted:
                run["annotations"] = {"color": "orange", "bold": True}
            runs.append(run)
    if not runs:
        runs = [{"type": "text", "text": {"content": ""}}]
    return {"rich_text": runs[:100]}          # Notion caps a property at 100 runs


def prop_number(value) -> dict:
    return {"number": value}


def prop_select(name: str | None) -> dict:
    return {"select": {"name": name} if name else None}


def prop_url(url: str | None) -> dict:
    return {"url": url or None}


def read_title(page: dict, name: str) -> str:
    node = page.get("properties", {}).get(name, {})
    return "".join(part.get("plain_text", "") for part in node.get("title", []))


def read_text(page: dict, name: str) -> str:
    node = page.get("properties", {}).get(name, {})
    return "".join(part.get("plain_text", "") for part in node.get("rich_text", []))


def read_number(page: dict, name: str):
    return page.get("properties", {}).get(name, {}).get("number")


def read_url(page: dict, name: str):
    return page.get("properties", {}).get(name, {}).get("url")


def read_select(page: dict, name: str):
    node = page.get("properties", {}).get(name, {}).get("select")
    return node.get("name") if node else None
