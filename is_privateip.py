import ipaddress
print(ipaddress.ip_address('1000:2000:3000:4000:5000:6000:7000:8000').is_private)
print(ipaddress.ip_address('192.168.0.1').is_private)