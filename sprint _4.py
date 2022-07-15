import csv
import time

dniUsuario=input("Ingrese su dni: ")

listasUsuario = []
cheques= []
#Abro el archivo csv
with open('sprint.csv') as File:
    reader = csv.DictReader(File)
    #Se lee el archivo csv y se lo introduce a una tupla
    for row in reader:
        listasUsuario.append(row)
        #Se filtran las listas que contengan el dni ingresado por el usuario
        usuario= list(filter(lambda item: item['DNI'] == dniUsuario, listasUsuario))
    #Creo un contador para recorrer cada una de las listas almacenadas en listasUsuario y almacenar los numero de cheques en cheques
    #Utilice esa forma de contar los objetos ya que si dejaba solamente len(usuario) me daba fuera de rango y con eso pude correjir ese error
        for i in range(len(listasUsuario)+len(usuario)-len(listasUsuario)):
            datos= usuario[i]
            cheques.append(datos['NroCheque'])
        
#creo una funcion para buscar si se repite algun numero, ese numero quede almacenado en repetidos
repetidos=[]
archivo=[]
for n in cheques:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)

#Fecha de impresion
def tiempoImpresion():
    fecha=time.strftime("%H:%M:%S")
    hora=time.strftime("%d/%m/%y")


#Creo un condicional para imprimir en pantalla o en un archivo csv, segun dese el usuario
#Impresion en pantalla



    #Condicional para que si no hay ningun numero repetido se ejecute el codigo
def impresoinPantalla():
    if(len(repetidos)==0):
        for i in range(len(listasUsuario)+len(usuario)-len(listasUsuario)):
            datos= usuario[i]
            print("Usuario: "+datos['DNI']+" Nro de cheque: "+datos['NroCheque']+" Tipo de cheque: "+datos['Tipo']+" Estado del cheque: "+datos['Estado'])
    else:
        print("ERROR: Existe mas de un cheque identico")

def impresionCSV():
    print(listasUsuario)
    archivo = open("dinosaurio.csv", "w", newline='')
    spamreader = csv.writer(archivo)
    spamreader.writerow(listasUsuario)
    archivo.close()   


impresion =int(input("Desea imprimir los datos en pantalla(Ingrese 1)/archivo CSV(Ingrese 2): "))

if(impresion==1):
    impresoinPantalla

if(impresion==2):
    impresionCSV 

else:print("ERROR")





























