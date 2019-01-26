import difflib
import collections
from collections import deque
import sys
import calendar
import heapq

pq = []

heapq.heappush(pq,(1,'HOLA'))
heapq.heappush(pq,(2," MUNDO"))

print(heapq.heappop(pq))
print(heapq.heappop(pq))

ab = {"HOLA":540,"H":47}
ac = {"HK":8,"o":7}

map1 = collections.ChainMap(ab,ac)

a = ["H\n","J\n","A\n"]
b = ["N\n","M\n","L\n"]

map1.new_child(a)

print(map1.parents)

a.append("N\n")

comparacion = difflib.context_diff(a,b,fromfile="a.py",tofile="b.py")

sys.stdout.writelines(comparacion)

dicts = {"A":47,"B":"Rojo","C":3}
dicts2 = {"D":47,"E":"Rojo","F":3}
fileList = {54:"JJ","HL":74}

dictFin = collections.ChainMap(dicts,dicts2)

print(list(dictFin.maps))

nChainMap = dictFin.new_child(fileList)

print(list(dictFin.parents))

listNew = ["ds","ds",47,47,45,45,21,"v","v"]

listModif = collections.Counter(listNew)
print(dict(listModif))

b = collections.Counter(v=5,a=8,n=5)

print(sorted(b.elements()))

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

comparation = (difflib.Differ().compare(texto1.splitlines(),texto2.splitlines()))

sys.stdout.writelines("\n".join(comparation))