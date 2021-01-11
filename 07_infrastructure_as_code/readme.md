# AWS Cli and profile
```bash
apt install awscli
aws configure
===> Enter access key and secret
```

# Terraform 
```bash
cd aws_instance
terraform init
terraform apply
```

# Install ansible ec2 dynamic inventory
```bash
sudo pip3 install boto3
ansible-galaxy collection install amazon.aws
```

# Ansible run
```bash
cd ansible
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook web_servers.yml -i dynamic_inventory
```