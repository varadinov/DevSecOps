# Create machine with terraform
```bash
cd aws_instance
terraform init
terraform apply
```
# Connect to machine
* Use the ssh key from terraform output
* ssh ec2-user@<MachineIp>

# Install docker
```bash
amazon-linux-extras install docker -y
systemctl start docker 
systemctl enable docker
```

# Run docker container 
```bash
docker run -d -p 8080:8080 -p 50000:50000 --name=jenkins jenkins/jenkins:lts
docker logs jenkins -f
```
**Note:** This example is not good for production. You have to mount the jenkins data to a persistante locaton.

# Configuration jenkins
* Set initial password
* Select suggested plugins
* Configure admin user and password
* Finish the setup

# Create pipeline job using git SCM
* Create git repository in github.com
* Upload jenkins directory content
* Create pipeline job using your git repository as SCM
* Run your job