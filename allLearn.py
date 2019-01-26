import datetime
import difflib
import textwrap
import calendar
import collections
import heapq
import sys
import nmap
import bisect
import copy
import pprint
from enum import Enum,unique, auto
import numbers

hoy = datetime.datetime.today()

def debug(f):
    def new_function(a, b):
        print("Function add() called!")
        return f(a, b)

    return new_function


@debug
def add(a, b):

    print(isinstance(a,numbers.Number))
    return a + b


print(add(7, 5))

print(datetime.datetime.today()-hoy)

@unique
class Color(Enum):

    RED = auto()
    GREEN = auto()
    BLACK = auto()


print(repr(Color.BLACK.value))

def movements(source, target):
    ss = (source % 8, int(source / 8))
    print(ss)
    tt = (target % 8, int(target / 8))
    print(tt)
    if abs(ss[0]-tt[0]) == abs(ss[1]-tt[1]):
        return 1
    return 2

print(movements(4,18))
"""
list = [[41,21,54,84],8,7,4,2,3,5,49,1,3,5,7,4,54]


print(list,"\n")
list2 = copy.copy(list)

print(list2)
list.append(100)
print(list2,"    ",list)


list.sort()

bisect.insort(list, 25)
bisect.insort(list, 200)

print(list)
print(bisect.bisect_left(list,5))
"""
nm = nmap.PortScanner()

pprint.pprint(nm.scan("192.168.0.1-10","22-443"))

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()

        for port in lport:
            print('port : %s\tstate : %s\t with name: %s' % (port, nm[host][proto][port]['state'], nm [host][proto][port]["name"]))

lista = []
heapq.heappush(lista,(1,"Perro"))
heapq.heappush(lista,(0,"Vaca"))

print(heapq.heappop(lista))

lista.insert(2,"Gallina")
print(lista)


l1 = [54,51,845,15]
l2 = [741,512,84,48]

mC = collections.ChainMap(l1,l2)
print(mC.new_child([54,"ds"]))

cl = calendar.TextCalendar().formatyear(1998)
print(cl)

cl2 = calendar.LocaleTextCalendar(firstweekday=2)

print(cl2.formatyear(1998))
#Esto imprimirá su edad exactamente
print(datetime.date(1,1,1)+datetime.timedelta((datetime.date.today()-(datetime.date(1998,10,24))).days-396))

texto1 = """Antigua Roma:
Antigua Roma (en latín, Antiqua Rōma) designa la
entidad política unitaria surgida de la expansión de la ciudad
de Roma, que en su época de apogeo, llegó a abarcar desde Gran
Bretaña al desierto del Sahara y desde la península ibérica al
Éufrates. En un principio, tras su fundación (según la
tradición en 753 aC), Roma fue una monarquía etrusca. Más
tarde (509 aC) fue una república latina, y en 27 aC
se convirtió en un imperio."""

print(textwrap.fill(texto1,width=50))

texto2 = """Antigua Roma (en latín, Antiqua Rōma) designa la
entidad política unitaria surgida de la expansión de la ciudad
de Roma, que en su época de apogeo, llegó a abarcar desde Gran
Bretaña al desierto del Sahara y desde la península ibérica al
Éufrates. En un principio, tras su creación (según la
tradición en 753 a. C.), Roma fue una monarquía etrusca. Más
tarde (509 a. C.) fue una república latina, y en 27 a. C.
se convirtió en un imperio"""

text1D = texto1.splitlines()
text2D = texto2.splitlines()

comparar = difflib.Differ().compare(text1D,text2D)

sys.stdout.writelines("\n".join(comparar))
sys.stdout.writelines("\n")

convert1 = input("Digite lo que desee: ")
convert2 = input("Digite lo que desee: ")

s1 = (convert1.replace(" ","\n ")).split(" ")
s2 = (convert2.replace(" ","\n ")).split(" ")

sys.stdout.writelines(difflib.unified_diff(s1, s2, fromfile='before.py', tofile='after.py'))