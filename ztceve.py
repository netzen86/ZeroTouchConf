#!/usr/bin/env python3

import csv
from netmiko import ConnectHandler

def get_devices_from_file(device_file):
    # This function takes a CSV file with inventory and creates a python list of dictionaries out of it
    # Each dictionary contains information about a single device

    # creating empty structures
    device_list = list()
    #device = dict()

    # reading a CSV file with ',' as a delimiter
    with open(device_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')

        # every device represented by single row which is a dictionary object with keys equal to column names.
        for row in reader:
            device_list.append(row)

    print("Got the device list from inventory")
    print('-*-' * 10)
    print()

    # returning a list of dictionaries
    return device_list


def load_config(conf_name):
    
    ignore = ["duplex", "alias", "configuration", "version"]
    commands = []
    
    with open(conf_name) as f:
        for line in f:
            words = line.split()
            words_intersect = set(words) & set(ignore)
            if not line.startswith("!") and not words_intersect:
                if "interface" in line:
                    commands.append(line.strip())
                    commands.append("no shut")
                else:
                    commands.append(line.strip())
    
    return commands

def device_connect(device, config):
    #print(config)
    net_connect = ConnectHandler(
        host=device["ip"],
        port=device["port"],
        username=device["username"],
        password=device["password"],
        device_type=device["device_type"],
        secret=device["secret"])
    net_connect.find_prompt(delay_factor=20)
    #net_connect.send_command('\n', expect_string=r'.*>')
    net_connect.enable("enable")
    net_connect.config_mode("configure terminal")
    output = net_connect.send_config_set(config)
    net_connect.disconnect()
    return output


for device in get_devices_from_file("devices.csv"):
    #print(f"Device {device}")
    configuration = load_config(device["conf_name"])
    print(f"Configuration {configuration}")
    print(device_connect(device, configuration))
   
