#!/usr/bin/env bash
# Publish the kit as a NEW repository with ONE clean first commit. Never pushes.
#
# Why: the private source repo's history holds personal data. Rewriting history is less
# certain than starting clean, so the public repo begins from a single commit that
# contains only the kit, authored with a noreply address.
#
# Usage:
#   GIT_AUTHOR_EMAIL='<id>+<user>@users.noreply.github.com' tools/publish-clean.sh <target-dir> [remote-url]
#   (an @sg57.dev business address is also accepted; this machine's git identity guard decides which it allows)
#
# Steps: run all six checks here; copy kit/ to <target-dir>; init a repo on main; scan the copy
# for private data again (with LIFEOS_DENYLIST if set); make one commit; add the remote if given;
# print the manual steps that remain (tag after evals/results exists, branch protection, CI secret).
set -euo pipefail

KIT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:?target directory required}"
REMOTE="${2:-}"
AUTHOR_NAME="${GIT_AUTHOR_NAME:-SG57 Labs}"
AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:?set GIT_AUTHOR_EMAIL to a GitHub noreply or @sg57.dev address}"

case "$AUTHOR_EMAIL" in
  *@users.noreply.github.com|*@sg57.dev) ;;
  *) echo "refusing: GIT_AUTHOR_EMAIL must be a GitHub noreply address or an @sg57.dev address (never a personal mailbox), got $AUTHOR_EMAIL" >&2; exit 1 ;;
esac

if [ -e "$TARGET" ] && [ -n "$(ls -A "$TARGET" 2>/dev/null)" ]; then
  echo "refusing: $TARGET exists and is not empty" >&2
  exit 1
fi

echo "== checks in $KIT =="
( cd "$KIT" \
  && python tools/readability.py --manifest tools/human-facing.txt \
  && python tools/scan-private.py . \
  && python tools/check-consistency.py \
  && python tools/build-paste.py --check \
  && python tools/rule-trace.py \
  && python tools/vendor-lint.py )

echo "== copy =="
mkdir -p "$TARGET"
# copy everything in kit/ except scratch; .github and .gitattributes are included
( cd "$KIT" && tar --exclude='./.work' --exclude='./.git' -cf - . ) | ( cd "$TARGET" && tar -xf - )

echo "== scan the copy =="
( cd "$TARGET" && python tools/scan-private.py . )

VERSION="$(tr -d '[:space:]' < "$TARGET/VERSION")"

echo "== one clean commit =="
( cd "$TARGET" \
  && git init -q -b main \
  && git config user.name "$AUTHOR_NAME" \
  && git config user.email "$AUTHOR_EMAIL" \
  && git add -A \
  && git commit -q -m "[CR] feat: life os $VERSION" -m "Public kit, version $VERSION. One clean first commit; see CHANGELOG.md." \
  && git log --format='%h %an <%ae> %s' -1 )

if [ -n "$REMOTE" ]; then
  ( cd "$TARGET" && git remote add origin "$REMOTE" && echo "remote origin = $REMOTE (not pushed)" )
fi

cat <<EOF

Next, by hand:
  1. Create the empty public repository on GitHub; push: git -C "$TARGET" push -u origin main
  2. Protect main; require pull requests; CODEOWNERS is in place.
  3. Add the CI secret LIFEOS_DENYLIST_B64 (base64 of your private denylist).
  4. Run the evals, write evals/results/$VERSION.md, then tag v$VERSION. CI refuses the tag without fresh results.
  5. Point the sg57.dev page at the raw URLs of the tagged dist/ files.
EOF
