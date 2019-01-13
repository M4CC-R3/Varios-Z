import datetime
from datetime import date

hoy = datetime.datetime.now()

fechaNacimiento = date(1998,10,24)
fechaActual = date.today()

print(("Su edad es de: ",int((fechaActual-fechaNacimiento).days/365)))

print(datetime.datetime.now()-hoy)