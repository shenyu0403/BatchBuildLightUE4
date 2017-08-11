import os, json

from socket import *
# from ..Models.DB import slave

network = '192.168.2.'
slave = {}

def is_up(addr):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.01)

        if not s.connect_ex((addr, 135)):
            s.close()
            return 1

        else:
            s.close()

def SaveNetworkName():
    for ip in range(1, 256):
        addr = network + str(ip)
        if is_up(addr):
            print('%s \t- %s' %(addr, getfqdn(addr)))
            slave[addr] = getfqdn(addr)

    path_json = os.path.abspath(
        "BatchLightUE4/Models/network.json")
    with open(path_json, 'w') as f:
        json.dump(slave, f, indent=4)