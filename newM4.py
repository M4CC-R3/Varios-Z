from datetime import datetime
from datetime import date
from datetime import timedelta

hoy = datetime.now()
try:
    fechaNacimiento = input("Digite su fecha de nacimiento (YY-MM-DD): ")

except ValueError:
    print("Valores erroneos, verifique que halla digita"
          " el formato correcto (AÑO:MES:DIA)")
    exit()

fechaNacimiento = fechaNacimiento.split("-")

fechaNacimiento = date(int(fechaNacimiento[0]),int(fechaNacimiento[1]),int(fechaNacimiento[2]))
fechaActual = date.today()

restoDelta = timedelta((fechaActual-fechaNacimiento).days-396)
try:
    final = (str(restoDelta+date(1,1,1))).split("-")
except OverflowError:
    print("Error de fechas")
    exit()

año = int(final[0])
mes = int(final[1])
dia = int(final[2])

if mes == 12:
    año += 1
    mes = 0

print("Su edad es de: {0} Años, {1} Meses y {2} Dias".format(año,mes,dia))

print(datetime.now()-hoy)