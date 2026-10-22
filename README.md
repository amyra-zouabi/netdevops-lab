# NetDevOps Lab — Network Automation Project

A 10-device spine-leaf virtual lab built with Containerlab (FRRouting/Alpine), automated with Python (Netmiko, Nornir) and Ansible.

## What this does
- Deploys a 10-device spine-leaf topology (2 spines, 4 leafs, 4 hosts)
- Automatically backs up device configs (Nornir + Netmiko)
- Automatically configures IP addressing and OSPF routing (Ansible)
- Tracks config changes and drift over time with Git

## Tools used
Containerlab, Python, Netmiko, Nornir, Ansible, Git

## Structure
- `topology.yml` — lab topology definition
- `ansible-inventory.yml`, `configure_ips.yml`, `configure_ospf.yml` — Ansible automation
- `inventory/`, `config.yaml`, `nornir_all_devices.py`, `backup_configs.py` — Nornir/Netmiko automation
- `backups/` — saved device configs
