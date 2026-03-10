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
