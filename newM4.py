from datetime import datetime
from datetime import date
from datetime import timedelta

hoy = datetime.now()

fechaNacimiento = input("Digite su fecha de nacimiento (YY-MM-DD): ")

fechaNacimiento = fechaNacimiento.split("-")

fechaNacimiento = date(int(fechaNacimiento[0]),int(fechaNacimiento[1]),int(fechaNacimiento[2]))
fechaActual = date.today()

restoDelta = timedelta((fechaActual-fechaNacimiento).days-396)
final = (str(restoDelta+date(1,1,1))).split("-")

año = int(final[0])
mes = int(final[1])
dia = int(final[2])

print("Su edad es de: {0} Años, {0} Meses y {0} Dias".format(año,mes,dia))

print(datetime.now()-hoy)