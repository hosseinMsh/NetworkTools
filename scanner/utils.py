from ping3 import ping
from ipaddress import ip_address

def is_alive(ip):
    """
    Check if an IP address is alive using ping3.
    """
    response = ping(ip, timeout=1)  # Timeout set to 1 second
    return response is not None

def scan_ip_range(start_ip, end_ip):
    """
    Scan a range of IPs and return the list of alive IP addresses.
    """
    start = ip_address(start_ip)
    end = ip_address(end_ip)
    alive_ips = []

    for ip in range(int(start), int(end) + 1):
        current_ip = str(ip_address(ip))
        if is_alive(current_ip):
            alive_ips.append(current_ip)
            print(f"{current_ip} is alive!")
        else:
            print(f"{current_ip} is not reachable.")
    return alive_ips
