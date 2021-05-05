#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Usage: $0 <commit_hash>"
    exit 0
fi

SERVICE_NAME=mentor-matching
ACR_NAME=mentormatching
RES_GROUP=$ACR_NAME
COMMIT_HASH=$(git rev-parse $1)
CURRENT_HASH=$(git branch --show-current)


# Stash uncommited changes
git checkout $COMMIT_HASH
if [ ! $? -eq 0 ]; then
    echo "ERROR: Failed to git stash and checkout to $COMMIT_HASH"
    git checkout $CURRENT_HASH
    exit 1
fi

# Build image and push to Azure ACR
echo "\n========== Building and Pushing Image to ACR =========="
az acr build --registry $ACR_NAME --image $SERVICE_NAME:$COMMIT_HASH .
if [ ! $? -eq 0 ]; then
    echo "ERROR: Failed to build image and push to ACR"
    git checkout $CURRENT_HASH
    exit 1
fi

echo "\n========== Successfully built and pushed image:  $SERVICE_NAME:$COMMIT_HASH =========="
git checkout $CURRENT_HASH
