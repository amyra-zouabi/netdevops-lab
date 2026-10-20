from netmiko import ConnectHandler

devices = [
    {"name": "spine1", "ip": "172.20.20.10"},
    {"name": "spine2", "ip": "172.20.20.5"},
    {"name": "leaf1",  "ip": "172.20.20.7"},
    {"name": "leaf2",  "ip": "172.20.20.8"},
    {"name": "leaf3",  "ip": "172.20.20.4"},
    {"name": "leaf4",  "ip": "172.20.20.9"},
    {"name": "host1",  "ip": "172.20.20.6"},
    {"name": "host2",  "ip": "172.20.20.11"},
    {"name": "host3",  "ip": "172.20.20.2"},
    {"name": "host4",  "ip": "172.20.20.3"},
]

for device in devices:
    connection_params = {
        "device_type": "linux",
        "host": device["ip"],
        "username": "root",
        "password": "admin",
    }

    connection = ConnectHandler(**connection_params)
    output = connection.send_command('vtysh -c "show ip route"')
    connection.disconnect()

    print(f"===== {device['name']} ({device['ip']}) =====")
    print(output)
    print()
