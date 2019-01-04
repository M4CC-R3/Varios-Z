val = input("Digite el número o palabra  a convertir a binario: ")

confirmador = str.isdecimal(val)

if (confirmador == True):

	print((bin(int(val))).replace('b',''))

if (confirmador == False):

	for l in val:
		print((bin(ord(l)).replace('b','')), end='')

import nmap
nmScan = nmap.PortScanner()
nmScan.scan('216.58.222.196', '21-443')


nmScan.command_line()
for x in range(21,444):
	print("Host google con puerto: ",x,": ",nmScan['216.58.222.196'].has_tcp(x))

