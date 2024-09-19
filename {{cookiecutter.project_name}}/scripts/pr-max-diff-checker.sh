#!/bin/bash

# Script helps to block Pull Requests with exceeded number of changed lines of code.
# Firstly, it compares HEAD with source branch
# Then it counts changed lines of code, excluding specified files and respecting max lines of code

# Read first input arg or take default value - 500
MAX_CHANGED_LOC="${1:-500}"

# Second argument (source branch) is required
if [ -z "$2" ]; then
  echo "No remote source branch supplied"
  exit 1
else
  source_branch=$2
fi

# Parse such line `2 files changed, 18 insertions(+), 248 deletions(-)` and write to variable
changed_loc=$(git diff --shortstat ${source_branch} ':(exclude)*.lock' \
        | awk '{ print $4+$6 }' \
        | awk -F- '{print $NF}' \
        | bc)

if [[ $changed_loc -le $MAX_CHANGED_LOC ]]; then
  echo "✅ ${changed_loc} lines of code changed. It is allowed to create Pull Request"
  exit 0
else
  echo "❌ ${changed_loc} lines of code changed. It is more than allowed ${MAX_CHANGED_LOC}. Please divide changes into several branches"
  exit 1
fi
