# LAB03
In this lab you are going to understand how to use the molecule tool.

# Before you start
* You need to login to AWS either with a tool like aws-adfs or with IAM user credentials. You can find the ansible workstation setup guide [here](../../WORKSTATION.md)

# Molecule
Molecule is a project from the Ansible family which is designed to help with the the development and testing of Ansible roles. It provides support for testing with multiple instances, operating systems and distributions, virtualization providers, test frameworks and testing scenarios. Molecule encourages an approach that results in consistently developed roles that are well-written, easily understood and maintained.

# Why molecule?
When you create a new playbook or change an existing playbook, you will probably want to test your code before executing it to your real environment. Is everything ok with the change that you just implemented? Maybe you have a missing parameter on the new task that you created or maybe you have put a wrong configuration option in the web server config file? You cannot be sure about the answers of those questions if you really don't test them. Creating a test infrastructure (machines, security groups, etc.) could be time consuming and challenging task if you try to do it manually. You will need also to re-create this infrastructure on every test so you have predictable and correct results. Fortunately, molecule is here to help you. It can bring temp infrastructure for you, apply you code on it and then destroy it. In order to build the required infrastructure you just need to define the desired state in the molecule configs and use the molecule command line tool.

# Molecule Command Line Reference
molecule *command*

* create  
Create the required instance or instances for development and testing.

* converge  
Converge will execute the sequence necessary to converge the instances.

* idempotence  
Do a second converge which is ensuring that your code is idempontent

* lint  
Validate your code against best practices defined by Ansible and the community

* verify  
Run validation tests if have such defined.

* destroy  
Destroy the instances created during the create step

* test  
Run a full cycle which is destroying (if there are object from previous run), creating, converging, checking the idempotancy, linting, verifying and again destroying.

**Note:** There are more command and scenarios in molecule but they are for more advanced use cases. You can find more information in the official molecule documentation.

# Execute Molecule
```bash
user@computer$ molecule crate
user@computer$ molecule converge
user@computer$ molecule destroy
```