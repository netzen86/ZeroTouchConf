#!/usr/bin/env python3


from netmiko import ConnectHandler


def get_config(conf_name):
    
    ignore = ["duplex", "alias", "configuration", "version"]
    commands = []
    
    with open(conf_name) as f:
        for line in f:
            words = line.split()
            words_intersect = set(words) & set(ignore)
            if not line.startswith("!") and not words_intersect:
                commands.append(line.strip())
    
    return commands


device_dict = {
"ip" : "10.0.0.64",
"port" : "32784",
"username" : "cisco",
"password" : "cisco",
"secret" : "cisco",
"device_type" : "cisco_ios_telnet",
}

commands = ["hostname RviOS", "cdp run"]

net_connect = ConnectHandler(**device_dict)
net_connect.find_prompt()
net_connect.enable("enable")
net_connect.config_mode("configure terminal")
output = net_connect.send_config_set(get_config())

print(output)
net_connect.disconnect()
