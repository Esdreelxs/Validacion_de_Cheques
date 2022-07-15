import csv, time
import datetime
x = datetime.datetime.now()
ahora = time.strftime("%c")
fecha= "%s_%s_%s_AT_%s_%s" %(x.day, x.month, x.year, x.hour, x.minute)
dniUsuario="44099981"
listasUsuario=[1,2,3,4,5,6]
archivo = open( fecha+".csv", "w", newline='')
spamreader = csv.writer(archivo)
spamreader.writerow(listasUsuario)
archivo.close()   

print(fecha)