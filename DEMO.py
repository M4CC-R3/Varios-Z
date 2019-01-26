from datetime import datetime
import bisect

hoy = datetime.today()

lista = [2,5,4,7,9,9,12,2,3,5,1,0,231,5,7,9,5,8,4,0,3,21]

lista.sort()

bisect.insort(lista,100)
bisect.insort(lista,101)
bisect.insort(lista,81)


print(lista)

print(datetime.today()-hoy)