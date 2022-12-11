#!/usr/bin/env python3
import yaml
import os
from argparse import ArgumentParser

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def load_yaml(file_name):
    with open(file_name, 'r') as file:
        return yaml.load(file.read())

def save_to_yaml(file_name, inventory):
    with open(file_name, 'w') as file:
        file.write(yaml.dump(inventory, indent=4, Dumper=NoAliasDumper))

def build_inventory(servers):
    inventory = {
        "all": {
            "hosts": {},
            "children": {}
        }
    }

    for server in servers:
        inventory['all']['hosts'][server['address']] = server
        for group in server['groups']:
            if group not in inventory['all']['children']:
                inventory['all']['children'][group] = {
                    "hosts": {}
                }
            
            inventory['all']['children'][group]['hosts'][server['address']] = server
    
    return inventory

def main(hosts_list_file, target_inventory_file):
    try:
        print('Load hosts list from file')
        servers = load_yaml(hosts_list_file)
        
        print('Build inventory dictionary')
        inventory = build_inventory(servers)

        print('Save target inventory file')
        save_to_yaml(target_inventory_file, inventory)
    
    except Exception as e:
        print(f"Cannot generate inventory file. Error: {e.message}")
        raise
        

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--hosts_list_file', required=True, help='Path to the hosts-list-file')
    parser.add_argument('--target_inventory_file', required=True, help='Path to the target inventory file')
    args = parser.parse_args()
    
    main(args.hosts_list_file, args.target_inventory_file)

