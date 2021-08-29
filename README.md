This is the project for DevOps course conducted at Innopolis University 2021 fall semester.

# Quickstart: Running the project

## Docker

To run the projects run the following command in the shell:

```shell
cd ./app_python
docker-compose -p tymur-lysenko-devops up
```

After running the command the go to the http://localhost:5000/ to see the application returning current time.

# Development

## Running the project

### Docker

- [ ] TODO

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up
```

## Testing

- [ ] TODO

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up test 
```

## Automation scripts

There is `scripts/` folder that contains useful scripts to automate routine development tasks:

- `docker/` - scripts to manipulate `docker`-related stuff
  - `prepare-multiarch-build.sh` - prepares the local environment for multi-architecture builds. Needs to be run once and before running `build-bultiarch.sh` for the first time.
  - `build-bultiarch.sh` - builds the specified Dockerfile for multiple architectures and pushes the built image to registry

## Releasing

### Multi-architecture builds 

#### Useful links

- [Docker official multi-architecture build guide](https://docs.docker.com/desktop/multi-arch/)
- [Building multi-architecture Docker image](https://www.smartling.com/resources/product/building-multi-architecture-docker-images-on-arm-64-bit-aws-graviton2/)

#### Building for multiple architectures

0. (Run only once) Initialize local system to be able to perform multi-architecture builds
   ```shell
   ./scripts/docker/prepare-multiarch-build.sh
   ```
1. Build & push to registry
   ```shell
   ./scripts/docker/build-multiarch.sh sitiritis/devops_lab_1-2:latest ./app_python
   ```


# Dockerhub

- [ ] TODO: change to badge

[The image for the labs is available on dockerhub](https://hub.docker.com/r/sitiritis/devops_lab_1-2)
