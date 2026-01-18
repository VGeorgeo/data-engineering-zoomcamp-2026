
![alt text](image.png)

Docker lets you run an application together with everything it needs (libraries, system tools, runtime) without installing those things on your main system.

The simpliest run command: docker run hello-world 
Quit commands: Ctrl + D; exit()

-it (You can interactively type commands into the container. You get a terminal-like shell inside the container.)
--rm (Automatically remove the container when it exits) 
--entrypoint=bash or bash (Ignore the image’s default entrypoint and start bash instead)


Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.
What's the version of pip in the image?
```
docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13-slimpython3

pip -V
```
