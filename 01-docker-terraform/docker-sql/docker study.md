## Basics
**Containers** isolated processes for each of your app's components. Each component - the frontend React app, the Python API engine, and the database - runs in its own isolated environment, completely isolated from everything else on your machine. Containers are:
- Self-contained. Each container has everything it needs to function with no reliance on any pre-installed dependencies on the host machine.
- Isolated. Since containers run in isolation, they have minimal influence on the host and other containers, increasing the security of your applications.
- Independent. Each container is independently managed. Deleting one container won't affect any others.
- Portable. Containers can run anywhere! The container that runs on your development machine will work the same way in a data center or anywhere in the cloud!

**Container Image** - a standardized package that includes all of the files, binaries, libraries, and configurations to run a container. There are two important principles of images:
1. Images are immutable. Once an image is created, it can't be modified. You can only make a new image or add changes on top of it.
2. Container images are composed of layers. Each layer represents a set of file system changes that add, remove, or modify files.

Docker Official Images - a curated set of Docker repositories, serve as the starting point for the majority of users, and are some of the most secure on Docker Hub

**Image Registry** is a centralized location for storing and sharing your container images. It can be either public or private. Whereas a **repository** is a collection of related container images within a registry.

<img width="644" height="617" alt="image" src="https://github.com/user-attachments/assets/76812a6d-dc48-49ab-b4b0-42965dce644e" />

**Docker Compose** - tool that allow to use multiple docker run commands to start multiple containers simultaniously. With Docker Compose, you can define all of your containers and their configurations in a single YAML file. If you include this file in your code repository, anyone that clones your repository can get up and running with a single command.

**Dockerfile versus Compose File** - Dockerfile provides instructions to build a container image while a Compose file defines your running containers. Quite often, a Compose file references a Dockerfile to build an image to use for a particular service.


## Building Images
*Container Images* are composed of layers. And each of these layers, once created, are immutable. 

### Writing a Dockerfile
Some of the most common instructions in a Dockerfile include:

- ```FROM <image> | python:3.13``` - this specifies the base image that the build will extend.
- ```WORKDIR <path> | /usr/local/app``` - this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.
- ```COPY <host-path> <image-path> | requirements.txt ./``` - this instruction tells the builder to copy files from the host and put them into the container image.
- ```RUN <command> | pip install --no-cache-dir -r requirements.txt``` - this instruction tells the builder to run the specified command.
- ```ENV <name> <value>``` - this instruction sets an environment variable that a running container will use.
- ```EXPOSE <port-number> | 8080``` - this instruction sets configuration on the image that indicates a port the image would like to expose.
- ```USER <user-or-uid> | app``` - this instruction sets the default user for all subsequent instructions.
- ```CMD ["<command>", "<arg1>"] | ["python", "./src/script.pu"]``` - this instruction sets the default command a container using this image will run.

**Containerize new projects quickly with docker init** - The docker init command will analyze your project and quickly create a Dockerfile, a compose.yaml, and a .dockerignore, helping you get up and going. Since you're learning about Dockerfiles specifically here, you won't use it now.


### Build, tag, and publish an image

- ```docker build .``` - The final . in the command provides the path or URL to the build context. At this location, the builder will find the Dockerfile and other referenced files.
- ```[HOST[:PORT_NUMBER]/]PATH[:TAG] | docker build -t my-username/my-image . | docker image tag my-username/my-image another-username/another-image:v1``` - tagging images (-t or --tag)
- ```docker image ls``` - view the images
- ```docker push <name>``` - Push the image
- ```docker image history <name>``` - View the history (or how the image was created) 

### Multi-stage builds

Multi-stage builds introduce multiple stages in your Dockerfile, each with a specific purpose. Think of it like the ability to run different parts of a build in multiple different environments, concurrently. By separating the build environment from the final runtime environment, you can significantly reduce the image size and attack surface. This is especially beneficial for applications with large build dependencies.


## Running Containers

```docker run -d -p HOST_PORT:CONTAINER_PORT nginx | docker run -d -p 8080:80 nginx``` - Publishing a port provides the ability to break through a networking isolation by setting up a forwarding rule. As an example, you can indicate that requests on your host’s port 8080 should be forwarded to the container’s port 80

**The .env file** acts as a convenient way to set environment variables for your Docker containers without cluttering your command line with numerous -e flags. To use a .env file, you can pass --env-file option with the docker run command.

- ```HOSTNAME=2042f2e6ebe4```
- ```foo=bar``` -  sets an environment variable foo inside the container with the value bar
- ```docker run -e POSTGRES_PASSWORD=secret --memory="512m" --cpus="0.5" postgres``` - use the --memory and --cpus flags with the docker run command to restrict how much CPU and memory a container can use

### Container Volumes
Volumes are a storage mechanism that provide the ability to persist data beyond the lifecycle of an individual container. Think of it like providing a shortcut or symlink from inside the container to outside the container.

```docker volume create log-data```

```docker run -d -p 80:80 -v log-data:/logs docker/welcome-to-docker``` - When starting a container with the following command, the volume will be mounted (or attached) into the container at /logs. If the volume log-data doesn't exist, Docker will automatically create it for you.

The following commands will be helpful to manage volumes:
- ```docker volume ls``` - list all volumes
- ```docker volume rm <volume-name-or-id>``` - remove a volume (only works when the volume is not attached to any containers)
- ```docker volume prune``` - remove all unused (unattached) volumes

### Sharing files between a host and container
- If you want to ensure that data generated or modified inside the container persists even after the container stops running, you would opt for a ***volume***.
- If you have specific files or directories on your host system that you want to directly share with your container, like configuration files or development code, then you would use a ***bind mount***. It's like opening a direct portal between your host and container for sharing. ***Bind mounts are ideal for development environments where real-time file access and sharing between the host and container are crucial.***



