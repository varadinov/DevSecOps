# Docker
Docker is a platform for packaing, shipping, and running applications. It provides the ability to run applicatiosn n in isolated environments called containers. The isolation allows you to run many containers simultaneously on a given host. Containers ission is lightweight because it doesn't need extra load of a hypervisor and guest operating system. It runs directly within the os kernel isolating the processes in their virtual namepsaces. This means that containers are more optimized from performance perspecite than virtual machines. 

## Docker Engine
Docker Engine is a long-running server application which is running as a daemon on linux. The docker daemon is a client-server program and it has an api which provides communication interface to the application. The most common client is the docker cli tool. However, there are tons of applications which are integrating with the docker API and providing different functionallities.

## Docker cli client
The Docker cli client (docker) is the most common tool that users use to interact with the Docker daemon. When you execuete docker commands, the cli client sends them to the docker deamon, which is doing the actual job for you (e.g. download container, running container, etc.) . The Docker cli client can communicate with different docker hosts. So you can specify in its configuration to talk to docker daemon on a remote machine instead of the local deamon.

## Docker images
Images are read-only templates of your applications with all libraries and dependecies including the OS files. Usually, images are built on top of other images and extending the with additional software and configurations. For example, you base your image on the centos8 image and include your python web application with all the python libraries your application depends on.

You might create your own images or you might use other images crated by other people and published in docker registry. 

## Build Docker image
To build your own image, you have to create a Dockerfile which is defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image.

## Docker Registry


# LAB
## Create and login to docker host
```
vagrant up
vagrant ssh
```

## Run your first container
```
[root@docker vagrant]# docker run hello-world
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

## Examples
Run interactive centos7 container
```bash
docker run -it centos:7
```
List running containers
```bash
docker ps
```
List running containers + stopped containers
```bash
docker ps -a
```
Run nginx listening on port 80
```bash
docker run -p 80:80 -d nginx
```

Attach and look real-time output of the process
```bash
docker attach <container-id>
```

Exec interactive shell
```bash
docker exec -it <container-id> /bin/bash
```

Build image
```bash
docker build . -t mycontainer 
```