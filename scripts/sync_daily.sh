#!/bin/bash
# The daily pipeline, as launchd runs it.
#
# Not a wrapper for convenience: it exists for the three things a scheduled
# run needs that an interactive one does not -- somewhere to put the output,
# a way to tell the owner it broke, and a commit that touches only what the
# pipeline produced.

set -o pipefail

REPO="/Users/echoooooo/PycharmProjects/leetcode-journey"
LOGS="$REPO/logs"
LOG="$LOGS/sync-$(date +%Y-%m-%d).log"

mkdir -p "$LOGS"
cd "$REPO" || exit 1

# Fourteen days is long enough to look back at a failure that went unnoticed
# over a holiday, and short enough that nobody ever thinks about the folder.
find "$LOGS" -name 'sync-*.log' -mtime +14 -delete 2>/dev/null

notify() {
    /usr/bin/osascript -e "display notification \"$1\" with title \"LeetCode 同步失败\" sound name \"Basso\""
}

{
    echo "=== $(date '+%Y-%m-%d %H:%M:%S') 开始 ==="

    # A scheduled run must not commit onto whatever branch happened to be
    # checked out when the machine was left for the night. Found by running
    # this by hand from a feature branch, where it would otherwise have
    # committed there and pushed main.
    BRANCH="$(git rev-parse --abbrev-ref HEAD)"
    if [ "$BRANCH" != "main" ]; then
        echo "!!! 当前在 $BRANCH 分支，不是 main，跳过"
        notify "当前在 $BRANCH 分支，没有同步"
        exit 1
    fi

    if ! /usr/bin/env python3 -m lc_review.cli sync-all --apply; then
        echo "!!! sync-all 失败"
        notify "管线中断，日志：$LOG"
        exit 1
    fi

    # Only what the pipeline produces. A scheduled run happens while the owner
    # is asleep, and the working tree may hold half-finished edits that must
    # not be swept into a commit nobody watched.
    #
    # data_elements holds the element answers and the inferred technique tags,
    # which the pipeline rewrites as surely as it rewrites Problems. Leaving
    # them out did not just lose them: they stayed dirty and stopped the
    # rebase below, so the whole run failed at the last step.
    git add Problems app/content.json lc_review/data_elements
    if git diff --cached --quiet; then
        echo "没有内容变化，不提交"
    else
        if ! git commit -m "Daily sync: $(date +%Y-%m-%d)"; then
            notify "提交失败，日志：$LOG"
            exit 1
        fi
        # Rebase first: the owner may have pushed from this machine during the
        # day, and a scheduled job must never be the thing that forces.
        # --autostash so anything the owner left half-edited is set aside
        # and put back, rather than stopping a run that has already done its
        # work.
        if ! git pull --rebase --autostash origin main; then
            notify "pull --rebase 失败，日志：$LOG"
            exit 1
        fi
        if ! git push origin main; then
            notify "push 失败，日志：$LOG"
            exit 1
        fi
        echo "已推送"
    fi

    echo "=== $(date '+%Y-%m-%d %H:%M:%S') 完成 ==="
} >> "$LOG" 2>&1
