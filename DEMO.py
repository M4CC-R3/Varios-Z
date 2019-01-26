from datetime import datetime
import bisect

hoy = datetime.today()

lista = [2,5,4,7,9,9,12,2,3,5,1,0,231,5,7,9,5,8,4,0,3,21]

lista.sort()

lista.append(80)
lista.sort()
lista.append(60)
lista.sort()
lista.append(10)
lista.sort()
lista.append(20)
lista.sort()
lista.append(30)
lista.sort()
lista.append(5)
lista.sort()

print(lista)

print(datetime.today()-hoy)