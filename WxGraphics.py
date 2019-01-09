import nmap
import hashlib


print(hashlib.algorithms_available)

print(hash("mighty"))

val = input("Digite el número o palabra  a convertir a binario: ")



confirmador = str.isdecimal(val)

if (confirmador == True):

	print((bin(int(val))).replace('b',''))

else:

	for l in val:
		print((bin(ord(l)).replace('b','')), end='')
"""
nmScan = nmap.PortScanner()
nmScan.scan('216.58.222.196', '21-443')


nmScan.command_line()

lista = (54,2,41,5,"D","DS")

#print(list(enumerate(lista)))
"""
#print(hex(10))
#print(str(41) in str(41))
print("\n ",str.isalnum("jhn0"))
print("\n {0}".format(str.isdigit("541.2")))
#print("HOLA")


Hi = frozenset([54,51,54,51,"dsd","dsd"])

Hi2 = {"SD",510,54}
print("\n Theren't elements common: {0}".format(Hi2.isdisjoint(Hi)))

print("Every the element is on the set: ",Hi2.issubset(Hi))

print(Hi.difference(Hi2))

