import datetime
import calendar
personas = {}
nombres=[]
dnis=[]
fechas_nac=[]

cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    nombre = input("Nombre de la persona:")
    while nombre in personas:
        nombres.append(nombre)
        print("Persona ya existe.")
        nombre = input("Nombre de la persona:")
    dni = int(input("Ingrese su dni:"))
    while dni > 0 :
        dnis.append(dni)
        dni = int(input("Ingrese dni correctamente:"))
    fecha_nac = datetime.datetime.strptime(input("ingrese su fecha de nacimiento (AAAA/MM/DD): "),"%Y/%m/%d")
    fechas_nac.append(calendar.timegm(fecha_nac.timetuple()))
    
