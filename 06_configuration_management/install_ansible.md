# CentOS/RHEL/AmazonLinux
sudo yum install python3
sudo pip3 install ansible==2.9.16

ansible --version
ansible 2.9.16
  config file = None
  configured module search path = ['/home/ec2-user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.7/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.7.9 (default, Aug 27 2020, 21:59:41) [GCC 7.3.1 20180712 (Red Hat 7.3.1-9)]

# Ubuntu
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install ansible==2.9.16

ansible --version
ansible 2.9.16
  config file = None
  configured module search path = ['/home/ec2-user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.7/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.7.9 (default, Aug 27 2020, 21:59:41) [GCC 7.3.1 20180712 (Red Hat 7.3.1-9)]

# WSL access C:\ drive
* Install WSL Ubuntu from Windows Store
https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab

* You can find all your windows files in /mnc/<drive>
For example you can open **work** directory on your **c** drive by 
```bash
cd /mnt/c/work
```