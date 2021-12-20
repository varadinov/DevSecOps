# CentOS/RHEL/AmazonLinux
```bash
sudo yum install python3 sshpass 
python3 -m venv ~/ansible
source ~/ansible/bin/activate
pip3 install pip --upgrade
pip3 install ansible==2.9.16 molecule==3.0.8 awscli==1.22.24 boto3==1.20.24 boto==2.49.0 pywinrm
```

```bash
ansible --version
ansible 2.9.16
  config file = None
  configured module search path = ['/home/ec2-user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.7/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.7.9 (default, Aug 27 2020, 21:59:41) [GCC 7.3.1 20180712 (Red Hat 7.3.1-9)]

```

# Ubuntu
```bash
sudo apt update
python3 -m venv ~/ansible
source ~/ansible/bin/activate
sudo apt install python3 python3-pip pywinrm>=0.3.0 sshpass
pip3 install ansible==2.9.16 molecule==3.0.8 awscli==1.22.24 boto3==1.20.24 boto==2.49.0 pywinrm>=0.3.0
```

```bash
ansible --version
ansible 2.9.16
  config file = None
  configured module search path = ['/home/ec2-user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.7/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.7.9 (default, Aug 27 2020, 21:59:41) [GCC 7.3.1 20180712 (Red Hat 7.3.1-9)]
```

# WSL access C:\ drive
* Install WSL Ubuntu from Windows Store
https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab

* You can find all your windows files in /mnc/<drive>
For example you can open **work** directory on your **c** drive by 
```bash
cd /mnt/c/work
```


# Set AWS Credentials for Molecule
## Set credentilas
You need IAM user with access key
```
aws configure
```
## Test connection
```
aws iam get-user
```
