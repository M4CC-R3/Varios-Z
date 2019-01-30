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
from termcolor import colored
import math
from fractions import Fraction
from decimal import Decimal
import random
import warnings
import math
import itertools

for diferencia in itertools.accumulate([10, 50, 100,20], lambda a, b: b-a):
    print(diferencia, end = ' ')

lista = [3,5,7]

lista2 = list(map(lambda n:n ** 2, lista))

print(lista2)

serie1 = random.Random('p')
serie2 = random.Random('p')

for num in range(3):
    print(serie1.random(), serie2.random())



n = int(input("Ingrese un numero: "))
lista = list(range(2, n+1))
i = 0
while(lista[i]*lista[i] <= n):
    # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
    for num in lista:
        if num <= lista[i]:
            # Cada iteracion del while hace que el for comience desde el primer elemento.
            # Esto es para omitir los numeros primos ya encontrados
            continue
        elif num % lista[i] == 0:
            # Si un numero es divisible entre el elemento actual del while
            # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
            lista.remove(num)
        else:
            # Si no es divisible, entonces omitirlo (no hacer nada)
            pass
    i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

print (lista)

for numero in range(3):
    print(random.uniform(100, 105), end=' ')

for numero in range(3):
    print(random.random(), end=' ')

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

print(random.choice(regalos))

for serie in range(3):
    print('\nserie:', serie + 1)
    random.seed(serie)
    for sorteo in range(5):
        regalo = regalos[random.randint(0, 9)]
        print('Sorteo', sorteo + 1, ':', regalo)

random.seed(0)
for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)

print(random.randint(0, 9))

print(Fraction(355,113))
print(Fraction(-3,7)+Fraction(2,3))

print(math.fmod(1540,2120))
print(1540%2120)

print(abs(-81.4))

print (colored("HOLA","green"))


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
    ss = (source % 8, (source % 8))
    print(ss)
    tt = (target % 8, (target % 8))
    print(tt)
    if abs(ss[0]-tt[0]) == abs(ss[1]-tt[1]):
        return 1
    return 2

print(movements(7,14))
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