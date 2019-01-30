import difflib
import sys
l1 = ["HOLA","Mundo","mango","Fruta"]
l2 = ["HOLA","MUNDO","mango","carnes"]

l1f = list(map((lambda x : x+"\n"),l1))
l2f = list(map((lambda x : x+"\n"),l2))

comparation = difflib.unified_diff(l1f,l2f,fromfile="a.py",tofiledate="b.py")

sys.stdout.writelines(comparation)