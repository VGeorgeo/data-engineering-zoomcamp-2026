
![alt text](image.png)

Docker lets you run an application together with everything it needs (libraries, system tools, runtime) without installing those things on your main system.

The simpliest run command: docker run hello-world 
Quit commands: Ctrl + D; exit()

```
-it (You can interactively type commands into the container. You get a terminal-like shell inside the container.)
--rm (Automatically remove the container when it exits) 
--entrypoint=bash or bash (Ignore the image’s default entrypoint and start bash instead)
-v means mount a volume — it connects a directory or file on your host system to a path inside the container.
-v $(pwd)/test:/app/test, where pwd - expands to the absolute path of your current directory
```

Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.
What's the version of pip in the image?
```
docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13-slimpython3

pip -V # pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

docker build -t test:pandas .
```

### Simple Dockerfile with pip
```
# base Docker image that we will build on
FROM python:3.13.11-slim

# set up our image by installing prerequisites; pandas in this case
RUN pip install pandas pyarrow

# set up the working directory inside the container
WORKDIR /app
# copy the script to the container. 1st name is source file, 2nd is destination
COPY pipeline.py pipeline.py

# define what to do first when the container runs
# in this example, we will just run the script
ENTRYPOINT ["python", "pipeline.py"]
```
#### Explanation:

- FROM: Base image (Python 3.13)
- RUN: Execute commands during build
- WORKDIR: Set working directory
- COPY: Copy files into the image
- ENTRYPOINT: Default command to run
