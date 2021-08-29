#!/usr/bin/env bash

# !!! Needs to be executed only once per build environment if it is not already
# initialized.
#
# Prepares the local environment to be able to perform multi-architecture
# builds.

docker buildx create --name mbuilder
docker buildx use mbuilder
docker buildx inspect --bootstrap
