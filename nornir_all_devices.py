from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

result = nr.run(task=netmiko_send_command, command_string='vtysh -c "show ip route"')

for host_name, host_result in result.items():
    print(f"===== {host_name} =====")
    print(host_result.result)
    print()
