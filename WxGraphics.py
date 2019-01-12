import nmap
import hashlib
import difflib
import sys
import keyword
import math
import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)



sys.stdout.writelines("{:*^30}\n".format("Bienvenido"))

var = "ijklsdjksdksjd skadjnlksa jlsakdnjaidjcnj "
print(var.split())


pote = float(100)
base = float((3+(math.sqrt(5))))
result = base**pote
final = []
contadorDeLetrasa = 0

modific = str(result)[::-1]

for x in modific:
	contadorDeLetrasa +=  1
	final.append(x)
	if contadorDeLetrasa == 3:
		break;

print("".join(final[::-1]))

texto1 = """Antigua Roma:
Antigua Roma (en latín, Antiqua Rōma) designa la
entidad política unitaria surgida de la expansión de la ciudad
de Roma, que en su época de apogeo, llegó a abarcar desde Gran
Bretaña al desierto del Sahara y desde la península ibérica al
Éufrates. En un principio, tras su fundación (según la
tradición en 753 aC), Roma fue una monarquía etrusca. Más
tarde (509 aC) fue una república latina, y en 27 aC
se convirtió en un imperio."""

texto2 = """Antigua Roma (en latín, Antiqua Rōma) designa la
entidad política unitaria surgida de la expansión de la ciudad
de Roma, que en su época de apogeo, llegó a abarcar desde Gran
Bretaña al desierto del Sahara y desde la península ibérica al
Éufrates. En un principio, tras su creación (según la
tradición en 753 a. C.), Roma fue una monarquía etrusca. Más
tarde (509 a. C.) fue una república latina, y en 27 a. C.
se convirtió en un imperio"""

comparador = difflib.Differ().compare(texto1.splitlines(),texto2.splitlines())

sys.stdout.writelines("\n".join(comparador))

s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

sys.stdout.writelines(difflib.context_diff(s1, s2, fromfile='before.py', tofile='after.py'))

print(difflib.get_close_matches("forever",("hforevla","fore","foverJDS","forever"),n=4))


'''

print(hashlib.algorithms_available)
print((type("45.54").__name__))

print('Tiene en su cuenta: ${:,} COP'.format(6511))

print(hash("mighty"))

val = input("Digite el número o palabra  a convertir a binario: ")

confirmador = str.isdecimal(val) #That rectify if if it decimal

trans = None

def converBinADecimal(bin):
	finTran = 0
	y = -1

	for x in trans[::-1]:

		y += 1

		if x == "1":

			finTran += pow(2,y)

	return finTran


if (confirmador == True):

	trans = str((bin(int(val)))).replace('0b','')

	print("{0} : {1}".format(trans, converBinADecimal(trans)))
	
else:

	trans = []

	for l in val:
		trans.append(bin(ord(l)).replace('b', ''))

	print(trans)

#print(tuple(trans))
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

firDict = {"sd":53,53:"sd","HOLA":"MUNDO"}

#print("{53}".format(**firDict))

#firDict["HOLO"] = 4
#print(firDict)

print(zip('dls',("HOLA",53,"FIN")))


for align, text in zip('<^>', ('left', 'center', 'right')):

	print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

print('{0:*>16}'.format("HOLA"))

'''