# Create machine with terraform
```bash
cd aws_instance
terraform init
terraform apply
```
# Connect to machine
* Use the ssh key from terraform output
* ssh ec2-user@<MachineIp> -i ~/.ssh/id_rsa_terraform

# Install docker
```bash
sudo -s
amazon-linux-extras install docker -y
systemctl start docker 
systemctl enable docker
```

# Run docker container 
```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock -d -p 80:8080 -p 50000:50000 --name=jenkins jenkins/jenkins:lts
docker logs jenkins -f
```
**Note:** This example is not good for production. You have to mount the jenkins data to a persistante locaton.

# Configuration jenkins
* Set initial password
* Select suggested plugins
* Configure admin user and password
* Finish the setup

# Install docker in the Jenkins container
* First loging to the container shell
```bash
docker exec -it -u root jenkins /bin/bash
```
* Then execute the below script
```bash
apt update
apt install sudo
apt install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update
apt install docker-ce docker-ce-cli containerd.io
usermod -a -G docker jenkins
# Do not use this in production ;)
chmod a+rw /var/run/docker.sock
```

# Create pipeline job using git SCM
* Create git repository in github.com
* Upload jenkins directory content
* Create pipeline job using your git repository as SCM
* Run your job