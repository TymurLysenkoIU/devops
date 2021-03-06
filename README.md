[![Build docker image and push to registry](https://github.com/TymurLysenkoIU/devops/actions/workflows/build-image.yml/badge.svg)](https://github.com/TymurLysenkoIU/devops/actions/workflows/build-image.yml)

[![dockerhub-badge](https://img.shields.io/badge/Dockerhub-black?logo=docker)](https://hub.docker.com/r/sitiritis/iu-devops)

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

The project source code is located in `app_python/` folder. 

## Running the project

### Docker

`docker-compose.dev.yml` contains configuration to run the project locally for development purposes and enables to debug it. It can also be used as a python interpreter and corresponding dependencies environment by IDE-s.

It can also be run in terminal via:

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up
```

### Testing

All tests are located in `tests` python package. You can find out more in the `Testing` section of [PYTHON.md](app_python/PYTHON.md).

One can run the tests locally in docker via the following command:

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up test
```

### Static analysis

To run static analysis (`mypy` and `pylama`) on the whole project in docker use the following command:

```shell
./scripts/code/static_analysis.sh
```

#### mypy

`mypy` can be configured in `mypy.ini` file.

Run `mypy` on the whole project:

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up mypy
```

#### Pylama

`pylama` config is located in `pylama.ini`.

Run `pylama` on the whole project:

```shell
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up pylama
```

#### Formatting

`yapf` is used to format the python code. The style is located in `.style.yapf`

Format code for the whole project:

```shell
# Directly in docker
docker-compose -p tymur-lysenko-devops -f docker-compose.dev.yml up format

# Or via script (actually runs the above command)
./scripts/code/format.sh
```

## Automation scripts

There is `scripts/` folder that contains useful scripts to automate routine development tasks:

- `docker/` - scripts to manipulate `docker`-related stuff
  - `prepare-multiarch-build.sh` - prepares the local environment for multi-architecture builds. Needs to be run once and before running `build-bultiarch.sh` for the first time.
  - `build-bultiarch.sh` - builds the specified Dockerfile for multiple architectures and pushes the built image to registry
- `code/` - source code related scripts such as code formatting and static analysis 
  - `format.sh` - runs `yapf` to format source code (see the [Formatting section](#formatting))
  - `static_analysis.sh` - runs `pylama` linters and `mypy` type checker (see [mypy](#mypy) and [pylama](#pylama) sections) 
  - `test.sh` - runs tests (see [Testing](#testing) section)

## CI/CD

### Pull requests

When pull request is sent, on each push to the branch the CI process will run to ensure the code quality, mainly the following checks will run:

- `mypy` type checker (see [`mypy` section](#mypy))
- `pylama` linters (see [`Pylama` section](#pylama))
- tests (see [`Testing` section](#testing))
- code formatting (see [`Formatting` section](#formatting))

For more details see `ci` GitHub workflow.

### Merge to master

Once a pull request is merged to master, the CD workflow (`build-image`) will tag the last commit with the bumped version and the image will be built and pushed to registry for the 2 platforms `linux/amd64` and `linux/arm64`. 

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

# Jenkins

```shell
cd jenkins
docker-compose -p tymur-lysenko-devops up
```

# Terraform

## Login to Azure and create a service principal

1. Start the shell with azure cli tool
    ```shell
    cd terraform
    docker-compose run az bash
    ```
2. Login to azure (save the output of the command)
    ```shell
    az login
    ```
3. Create service principal (save the output of the command)
    ```shell
    az ad sp create-for-rbac --name iu-devops
    ```
4. Put the output of the commands to the `main.tf`:
    ```shell
    # Configure the Microsoft Azure Provider
    provider "azurerm" {
      features {}
    
      # Set valid values
      subscription_id   = "<azure_subscription_id>"
      tenant_id         = "<azure_subscription_tenant_id>"
      client_id         = "<service_principal_appid>"
      client_secret     = "<service_principal_password>"
    }
    ```

## Deploy the application container

Ensure that you have [logged in](#login-to-azure-and-create-a-service-principal).

```shell
terraform apply
```

# Ansible

Everything related to ansible infrastructure management is located under the `ansible/` directory.

## Prepare to run the roles (required to do before running anything via ansible)

0. `cd ansible`
1. Ensure that you have SSH access to the target host
2. Change host and user in inventory to the desired one (`inventory/hosts.yml`)

   ```yaml
   all:
    hosts:
      app:
        ansible_host: 127.0.0.1  # Set your host here
        ansible_user: root  # Set user to run playbooks under here
   ```

## Deploy the app on the target machine

```shell
ansible-playbook app.yml
```

## Deploy docker on the target machine

```shell
ansible-playbook docker.yml
```

## Roles description

### `app_python`

Starts the app in docker container on the target machine.

#### Variables

- `docker_compose_dir` - path, where docker-compose file for app deployment is being copied and ran.

#### Requirements

Requires facts to be gathered.

```yaml
gather_facts: true
```

### `docker`

Installs `docker` and `docker-compose`, creates the `docker` group and, if the `anisble_user` user is not `root` adds the user to the group (so that docker commands can be ran without `sudo`).

The supported distributions are:

- Ubuntu
- Debian


#### Requirements

Requires facts to be gathered.

```yaml
gather_facts: true
```
