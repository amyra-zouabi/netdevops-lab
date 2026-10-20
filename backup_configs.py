from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
import os

nr = InitNornir(config_file="config.yaml")

os.makedirs("backups", exist_ok=True)

result = nr.run(task=netmiko_send_command, command_string='vtysh -c "show running-config"')

for host_name, host_result in result.items():
    filename = f"backups/{host_name}_running-config.txt"
    with open(filename, "w") as f:
        f.write(host_result.result)
    print(f"Saved backup for {host_name} -> {filename}")
