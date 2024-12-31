import os
from ipaddress import ip_address

def is_alive(ip):
    response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")
    return response == 0

def scan_ip_range(start_ip, end_ip):
    start = ip_address(start_ip)
    end = ip_address(end_ip)
    alive_ips = []

    for ip in range(int(start), int(end) + 1):
        current_ip = str(ip_address(ip))
        if is_alive(current_ip):
            alive_ips.append(current_ip)

    return alive_ips
