import datetime
import difflib
import math
import textwrap
import calendar
import collections
import heapq
import logging
import sys

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

