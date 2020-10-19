# Vagrant
Vagrant tries to simplify the configuration management of virtual machines in order to increase productivity. It is simple an powersful tool provided as an open source project by HashiCorp. It leverages a declarative ruby dialect in configuration file (Vagrantfile) which describes all your requirements. Vagrant works on all three major platforms Windows, Mac and Linux.

# Vagrant Basic commands
# Creating a VM
vagrant up
**Note:** you may need to specify --provider=hyperv

## Getting into a VM
vagrant ssh -- connects to machine via SSH protocol
vagrant rdp -- connects to machine via RDP protocol
vagrant <ssh/rdp> <boxname> -- if you have more than one boxes, you have to specify the boxname

## Stopping a VM
vagrant halt -- stops the vagrant machines

## Removign a VM
vagrant destroy

