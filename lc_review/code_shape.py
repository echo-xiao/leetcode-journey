"""Whether two pieces of code are the same shape.

The question this answers is the owner's: "did the big structural logic
change". Comparing text cannot answer it -- renaming a variable would read as
a rewrite -- so the comparison is on the parsed syntax tree with every
identifier replaced by a positional placeholder.

The normalisation is alpha-equivalence: identifiers are numbered by first
appearance, while operators, literals and attribute names stay in the tree. So
two programs collide only when renaming makes them identical, and renaming
preserves meaning -- "same shape, different behaviour" is not a case that
arises outside deliberately shadowed scopes.

The error is on the other side. A `for` rewritten as a `while`, or two
independent statements swapped, reads as a new shape though the approach is
unchanged, and costs one wasted regeneration. Using a model to rule those out
would spend a call to save a call.
"""

from __future__ import annotations

import ast
import hashlib


def _without_docstring(body: list[ast.stmt]) -> list[ast.stmt]:
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        return body[1:]
    return body


class _Canonicalise(ast.NodeTransformer):
    """Rename identifiers to v0, v1, ... in order of first appearance."""

    def __init__(self) -> None:
        self._slots: dict[str, str] = {}

    def _slot(self, name: str) -> str:
        return self._slots.setdefault(name, f"v{len(self._slots)}")

    def visit_Name(self, node: ast.Name) -> ast.AST:
        node.id = self._slot(node.id)
        return self.generic_visit(node)

    def visit_arg(self, node: ast.arg) -> ast.AST:
        node.arg = self._slot(node.arg)
        node.annotation = None
        return self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.AST:
        # `total: int = 0` becomes `total = 0`. Stripping the annotation alone
        # is not enough: an annotated assignment is a different node type from
        # a plain one, so the two would still hash apart, and adding a type
        # hint is not a change of approach.
        if node.value is not None:
            replacement = ast.Assign(targets=[node.target], value=node.value)
            return self.generic_visit(replacement)
        node.annotation = ast.Constant(value=None)
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node.name = self._slot(node.name)
        node.returns = None
        node.body = _without_docstring(node.body)
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        node.name = self._slot(node.name)
        node.returns = None
        node.body = _without_docstring(node.body)
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        node.name = self._slot(node.name)
        node.body = _without_docstring(node.body)
        return self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> ast.AST:
        # Attribute names are left alone: `stack.pop` and `stack.append` are
        # different operations, not different spellings of one.
        return self.generic_visit(node)


def _normalised_text(code: str) -> str:
    """Trailing whitespace and blank lines removed, nothing else.

    The fallback for anything Python cannot parse -- Java, C++, a truncated
    response. Weaker than the AST route on purpose: guessing at another
    language's grammar would be worse than admitting the comparison is textual.
    """
    lines = [line.rstrip() for line in code.splitlines()]
    return "\n".join(line for line in lines if line)


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def shape_of(code: str) -> str:
    """A stable fingerprint of what this code does, not how it is spelled."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return _digest("text:" + _normalised_text(code))
    tree = _Canonicalise().visit(tree)
    ast.fix_missing_locations(tree)
    return _digest("ast:" + ast.dump(tree))


def shapes_of(codes: list[str]) -> set[str]:
    return {shape_of(code) for code in codes}


def has_new_shape(remote: list[str], local: list[str]) -> bool:
    """Does `remote` contain a shape `local` has never held?

    Asymmetric on purpose. Local can hold versions LeetCode no longer lists,
    and that is not a reason to redownload anything.
    """
    return bool(shapes_of(remote) - shapes_of(local))
