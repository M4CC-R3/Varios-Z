import difflib
import sys

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

text1c = texto1.splitlines()
text2c = texto2.splitlines()

comparador = difflib.Differ().compare(text1c,text2c)

sys.stdout.writelines("\n".join(comparador))