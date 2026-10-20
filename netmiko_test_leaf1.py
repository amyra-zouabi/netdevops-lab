from netmiko import ConnectHandler

device = {
    "device_type": "linux",
    "host": "172.20.20.7",
    "username": "root",
    "password": "admin",
}

connection = ConnectHandler(**device)

output = connection.send_command('vtysh -c "show ip route"')

print(output)

connection.disconnect()
