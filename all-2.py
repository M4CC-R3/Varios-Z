import nmap
import pprint
import random
import itertools

l = [47,5,7,5,6,9,7,1,2,65,84,87,59,2]


scan = nmap.PortScanner()
pprint.pprint(scan.scan(hosts="192.168.0.1/24",arguments="-A -T5",ports="21-443"))

for x in scan.all_hosts():

    print('----------------------------------------------------')

    print("Host: %s \nState: %s" % (x,scan[x].state()))

    for y in scan[x].all_protocols():

        print("Protocolo: ", y)

        lsport = scan[x][y].keys()

        for z in lsport:

            print("Puerto: %s\n State: %s\t Port_Name: %s" % (z,scan[x][y][z]["state"],scan[x][y][z]["name"]))