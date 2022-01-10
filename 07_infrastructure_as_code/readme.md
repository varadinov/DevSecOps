# Ansible and AWS CLI Setup
Please refer to the installation in chapter 6. Configuration Managemenet.

# Install terraform
Go to the terrform download page https://www.terraform.io/downloads
Follow the instructions for installation of the specific version and operating system  

Example for linux installation:
```bash
cd  /usr/local/bin
wget https://releases.hashicorp.com/terraform/1.1.3/terraform_1.1.3_linux_amd64.zip
unzip terraform_1.1.3_linux_amd64.zip
rm terraform*.zip
```

# Terraform 
```bash
cd terraform
terraform init
terraform apply
```

# Ansible run
You need first to active your ansible virtual environment (Follow chapter 6. Configuration Management)
```bash
cd ansible
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook web_servers.yml -i dynamic_inventory/ --key-file ~/.ssh/id_rsa_terraform
```