import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)
print(endereco + 1)
print(endereco + 256)

ip2 = '192.168.0.0/4'

rede = ipaddress.ip_network(ip2,strict=False)
for ip2 in rede:
    print(ip2)