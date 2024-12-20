#!/bin/bash

# Get the list of dangling blobs, trees, and commits
dangling_blobs=$(git fsck --lost-found | grep 'dangling blob' | awk '{print $3}')
dangling_trees=$(git fsck --lost-found | grep 'dangling tree' | awk '{print $3}')
dangling_commits=$(git fsck --lost-found | grep 'dangling commit' | awk '{print $3}')

# Initialize counter for file naming
counter=1

# Loop through each dangling blob and recover its content
for blob in $dangling_blobs; do
    git cat-file blob $blob >"recovered-file-$counter"
    counter=$((counter + 1))
    echo "Recovered blob $blob into recovered-file-$counter"
done

# Loop through each dangling tree and recover its content
for tree in $dangling_trees; do
    git cat-file tree $tree >"recovered-tree-file-$counter"
    counter=$((counter + 1))
    echo "Recovered tree $tree into recovered-tree-file-$counter"
done

# Loop through each dangling commit and recover its content
for commit in $dangling_commits; do
    git cat-file commit $commit >"recovered-commit-file-$counter"
    counter=$((counter + 1))
    echo "Recovered commit $commit into recovered-commit-file-$counter"
done

echo "Recovery completed for all dangling objects."
