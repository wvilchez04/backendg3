import datetime

age = int(input("¿Cuál es tu edad? "))
hora= int(datetime.datetime.now().strftime('%H'))
if age < 18: 
    if(hora > 18):
        print ("Debe ir a dormir.")
    else:
        print("Usted tiene que hacer su tarea.")
else:
    print("No estas obligado a hacer nada.")