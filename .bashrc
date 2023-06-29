#!/bin/bash

commit_message="$1"

# Function to run git add, commit, and push
function git_commit_and_push() {
  git add .
  git commit -m "$commit_message"
  git push
}

# Call the function
git_commit_and_push