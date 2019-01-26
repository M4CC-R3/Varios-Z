from datetime import datetime
from datetime import date
from datetime import timedelta

hoy = datetime.now()

fechaNacimiento = input("Digite su fecha de nacimiento (YY-MM-DD): ")

fechaNacimiento = fechaNacimiento.split("-")

try:
    fechaNacimiento = date(int(fechaNacimiento[0]),int(fechaNacimiento[1]),int(fechaNacimiento[2]))
except:
    print("Valores erroneos, verifique que halla digitado"
          "\n el formato y orden especificado (AÑO-MES-DIA)")
    exit()

fechaActual = date.today()

restoDelta = timedelta((fechaActual-fechaNacimiento).days-396)

try:
    final = (str(restoDelta+date(1,1,1))).split("-")
except OverflowError:
    print("Error de fechas, asigne una fecha realista o consulte \n"
          "con el programador si las fechas son compatibles")
    exit()

año = int(final[0])
mes = int(final[1])
dia = int(final[2])

if mes == 12:
    año += 1
    mes = 0

print("Su edad es de: {0} Años, {1} Meses y {2} Dias".format(año,mes,dia))

print(datetime.now()-hoy)