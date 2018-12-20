import ipaddress
print(int(ipaddress.ip_address('1.2.3.4')))
print(ipaddress.ip_address(16909060).__str__())

print(int(ipaddress.ip_address(u'1000:2000:3000:4000:5000:6000:7000:8000')))

print(ipaddress.ip_address(21268296984521553528558659310639415296).__str__())
