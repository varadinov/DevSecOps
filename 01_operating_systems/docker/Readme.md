# Docker
Docker is a platform for packaging, shipping, and running applications. It provides the ability to run applications in isolated environments called containers. The isolation allows you to run many containers simultaneously on a given host. Containers isolation is lightweight because it doesn't need extra load of a hypervisor and guest operating system. It runs directly within the os kernel. It is isolating the processes in virtual namespaces. For this reason, the containers are more optimized from performance perspective than virtual machines. 

## Docker Engine
Docker Engine is a long-running server application which is running as a daemon on linux. The docker daemon is a client-server program and it has an api which provides communication interface to the application. The most common client is the docker cli tool. However, there are tons of applications which are integrating with the docker API and providing different functionalities.

## Docker cli client
The Docker command line interface (CLI) client (docker) is the most common tool that users use to interact with the Docker daemon. When you execute docker commands, the CLI client sends them to the docker daemon, which is doing the actual job for you (e.g. download container, run container, etc.) . The Docker CLI client can communicate with different docker hosts. So you can configure it to talk to docker daemon on a remote machine instead of the local daemon.

## Docker images
Images are read-only templates of your applications with all libraries and dependencies including the OS files. Usually, images are built on top of other images and extending the with additional software and configurations. For example, you base your image on the centos8 image and include your python web application with all the python libraries your application depends on.  
  
You might create your own images or you might use other images crated by other people and published in docker registry. 

## Build Docker image
To build your own image, you have to create a Dockerfile which is defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image.

## Docker Registry
A Docker registry is a storage and distribution system for docker images. It is organized into Docker repositories, where a repository holds all the versions (tags) of a specific image. It allows you to pull images locally, as well as push new images to it. The default docker engine registry is DockerHub (The Docker’s public registry instance). However, it is possible to run your own docker registry, as well as to use a commercially supported version provided as a service. There are many public registries available online with their advantages and disadvantages. For example, in AWS you can use 
their own docker registry implementation Elastic Container Registry (ECR). 

# Docker in action

## Run your first container
```
[root@my-machine]# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete
Digest: sha256:8c5aeeb6a5f3ba4883347d3747a7249f491766ca1caa47e5da5dfcf6b9b717c0
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
```
## Basic Docker commands
**docker run** creates and starts a container in one operation
**docker start** starts a container so it is running
**docker stop** stops a running container
**docker restart** stops and starts a container
**docker wait** blocks until running container stops
**docker attach** will connect to a running container
**docker exec** to execute a command in container
**docker ps** shows running containers
**docker logs** gets logs from container
**docker inspect** looks at all the info on a container
**docker images** shows all images
**docker rmi** removes an image
**docker build** creates image from Dockerfile

# Labs
* Run interactive ubuntu:22.04 container.  
Note: -it (-i -t) is interactive terminal (tty)
```bash
docker run -it --name my_ubuntu_container ubuntu:22.04
```

* List running containers
```bash
docker ps
```

* List running containers + stopped containers
```bash
docker ps -a

```
* Run nginx listening on port 80  
Note: -d is detach from the running container
```bash
docker run -p 80:80 -d nginx
```

* Attach and look real-time output of the process  
Note: you can detach with CTRL+P followed by CTRL+Q
```bash
docker attach <container-id>
```

* Exec interactive shell to a running container
```bash
docker exec -it <container-id> /bin/bash
```


* Create docker image manually
In this exercise you are modifying and existing container and saving it to a new image.  
Note: This is not the recommended approach to create new images! The best practice is to use a Dockerfile to describe all the steps required to create new image.

```bash
# run nginx container from the official nginx image and configure host port 8009 to redirect to the container port 80
docker run -p 8089:80 --name manual_update_nginx -d nginx 
# List containers
docker ps
# Execute /bin/bash in the container. This will open a new shell in the context of the nginx container
docker exec -it manual_update_nginx /bin/bash
# Modify the index.html file
echo "<h1>Hello, This is my NGINX</h1>" > /usr/share/nginx/html/index.html
press CTRL+D
# Commit the modified container to a new image
docker commit manual_update_nginx my_nginx
# See the images
docker images
# Run new container form the new image
docker run -p 8010:80 -d my-nginx
```

* Create new image using Dockerfile.  
In this exercise you are creating a new image using a Dockerfile. This is the recommended approach for image creation.

- Review the docker file
```Dockerfile
FROM python:3.10     # -----> Use python version 3.10 image as base image
RUN pip3 install "fastapi[all]"    # -----> Install python fastapi framework
WORKDIR /app   # ----> Creating working directory in the image
ADD main.py /app/   # -----> Copy our fastapi application to the image
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000   # -----> execute this command when you run a container
```

- Build the docker image from the Dockerfile in the current directory
```bash
cd fastapi_simple_project
docker build . -t fastapi_simple_project
docker run -p 8099:8000 -d --name fastapi_simple_project fastapi_simple_project:latest
cd ../
```

* Run container with mounted directory from the host file system
```bash
mkdir /tmp/my_container_data
cd fastapi_simple_project 
docker build . -t fastapi_simple_project
docker run -p 8100:8000 -d --name fastapi_write_project --mount src=/tmp/my_container_data,target=/data,type=bind fastapi_simple_project:latest
cd ../
```