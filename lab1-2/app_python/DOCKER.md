# Docker

## Good practices

### 1. Specify versions of the images used

Thus, there won't be unexpected problems, if new version that is incompatible with the previous is issued.

### 2. Use docker-compose

There won't be need in managing docker's local infrastructure with multiple commands, instead docker-compose provides an easy and reliable interface to work with docker.

### 3. Use .dockerignore

In order not to copy unnecessary files in the image, specify files that are not needed in `.dockerignore` file.
