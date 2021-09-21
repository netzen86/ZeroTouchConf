#!/usr/bin/env python3

import csv
import time
import telnetlib
from netmiko import ConnectHandler
from netmiko.ssh_dispatcher import redispatch

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
    
    return commands():
        telnet.write(b'\n')
>>> telnet.write(b'super\n')
>>> telnet.write(b'super\n')
>>> telnet.write(b'y\n')
>>> telnet.write(b'super\n')
>>> telnet.write(b'nihilant\n')
>>> telnet.write(b'nihilant\n')
>>> telnet.read_very_eager().decode()



def connect_huawei_console()

def device_console_connect(device, config):
    repeater = False
    try:
        with ConnectHandler(
            host=device["ip"],
            port=device["port"],
            device_type=device["device_type"]) as console:
            while not repeater:
                console.write_channel('\r\n')
                output = console.read_until_pattern("yes|>")
                print("Found yes/no")
                if "yes" in output:
                    console.write_channel('no\n')
                    #time.sleep(1)
                console.write_channel('\r\n')
                #time.sleep(0.5)
                #console.write_channel('\r\n')
                console.read_until_pattern(">")
                #print("Loading finished")
                #console.write_channel('\r\n')
                #time.sleep(1)
                console.write_channel('show clock\n')
                output = console.read_until_pattern(">")
                print(output)
                redispatch(console, device_type='cisco_ios_telnet')
                output = console.send_command("show clock")
                print("REDISPATCH SUCCESS", output)
                console.enable()
                console.send_config_set(config)
                repeater = True
        return output
    except:
        print("error")




def device_connect(device, config):
    with ConnectHandler(
        host=device["ip"],
        port=device["port"],
        username=device["username"],
        password=device["password"],
        device_type=device["device_type"],
        secret=device["secret"]) as net_connect:
        net_connect.enable()
        output = net_connect.send_config_set(config)
    return output

""" def device_connect(device, config):
    #print(config)
    net_connect = ConnectHandler(
        host=device["ip"],
        port=device["port"],
        username=device["username"],
        password=device["password"],
        device_type=device["device_type"],
        secret=device["secret"])
    net_connect.enable("enable")
    output = net_connect.send_config_set(config)
    return output
 """

for device in get_devices_from_file("devices.csv"):
    print(f"Device {device}")
    configuration = load_config(device["conf_name"])
    print(f"Configuration {configuration}")
    print(device_console_connect(device, configuration))
   
