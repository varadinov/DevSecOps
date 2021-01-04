# LAB04
In this lab you are going to see a two tier setup of a simple php application which is using mariadb

# Before you start
* You need to login to AWS either with a tool like aws-adfs or with IAM user credentials. You can find the ansible workstation setup guide [here](../../WORKSTATION.md)
* You will need to execute molecule create. Molecule will create three machines for you, so you can experiment on them.

```bash
user@computer$ molecule create
```

# Run the myapp.yml playbook
The playbook is building a simple demo purpose php application which is using mariadb as a database. The playbook contains three plays:
* Apply common configuration to all nodes
  * We are setting up a ntp client on all the servers from our inventory. This is a common configuration so that's why we are doing it on all the servers.
* Configure and deploy the webservers and application code
  * We are targeting only the webservers and installing on them httpd, apache, php and also we are deploying our app code (index.php). 
  * For the purpose of this demo we have a simple php page. However, ansible is putting connection information to our database server.
* Deploy MariaDB and configure the databases
  * We are targeting only the database servers and installing and configuring mariadb on them (Open Source fork of MySQL made by the original MySQL developers)
  * We are creating username and password which are used by the web servers.
  * We are also creating a hedgeservdb database which we will see when we open the web servers with browser.

```bash
user@computer$ ansible-playbook myapp.yml -i inventory/
```
**Note:** When we called the *molecule create* command, it generated a static inventory file (inventory/hosts.yml) for us. For this reason we are passing *-i inventory/* as parameter. Ansible will use the inventory fail and group variables from this directory.

# Clean up
Do not forget to clean your servers!
```bash
user@computer$ molecule destroy
```