#!/usr/bin/env bash

# Builds dockerfile with a specified image name and tag for multiple
# architectures and pushes the built images to the registry.
#
# Usage
# ./build-multiarch.sh image-name:tag /build/context [/path/to/dockerfile]
#
# Arguments:
# $1 (required) - image name and tag to be used for the build
# $2 (required) - context to be used for the build (by default Dockerfile in
#                 the context will be used to build the image)
# $3 (optional) - path to Dockerfile to be used to build the image

IMAGE_NAME="{$1:?The first argument must be image name and tag, e.g. image-name:tag}"
BUILD_CONTEXT="{$2:?The second argument must be a path to docker build context, e.g. /path/to/build/context}"
DOCKERFILE_PATH="{$3:$BUILD_CONTEXT/Dockerfile}"

docker buildx build \
  --tag="$IMAGE_NAME" \
  --push \
  --platform linux/amd64,linux/arm64 \
  --file="$DOCKERFILE_PATH"
  "$BUILD_CONTEXT"
