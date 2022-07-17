import csv
from datetime import datetime
entrada=""
listaUsuario=[] 
#Guarda archivos csv
archivoCSV=[]  
#Numeros de cheques
numerosCheques=[]
#Abre archivo csv 
with open('sprint.csv') as File:
    reader = csv.DictReader(File)

    dniCliente=input("Ingrese el numero su numero de DNI: ")
    #condiconal para la impresion en pantalla o en csv
    opcion=int(input("Para imprimmir los datos en Pantalla(Ingrese 1)/Archivo CSV(Ingrese 2)"))

    #Bucle para recorrer el csv
    for row in reader:
        listaUsuario.append(row)


#Filtra el dni ingresado
usuario=(list(filter(lambda item: item['DNI'] == dniCliente, listaUsuario)))

archivoCSV.append("NumeroCuentaDestino,Valor,FechaOrigen,FechaPago\n")
#fecha y numero de cheque
for i in range(len(usuario)+len(usuario)-len(usuario)):
    datos= usuario[i]
    origen=int(datos['FechaOrigen'])
    pago=int(datos['FechaPago'])
    origen= str(datetime.fromtimestamp(origen))
    pago=str(datetime.fromtimestamp(pago))
    num=int(datos['NroCheque'])
    numerosCheques.append(num)
    archivoCSV.append(datos['NumeroCuentaDestino']+datos['Valor']+origen+pago+"\n")

#Impresion en pantalla
def impresionPantalla():
    for i in range(len(usuario)+len(usuario)-len(usuario)):
        datos= usuario[i]
        print("Usuario: "+datos['DNI']+" Nro de cheque: "+datos['NroCheque']+" Tipo de cheque: "+datos['Tipo']+" Estado del cheque: "+datos['Estado'])
    
#impresion en CSV
def impresionCSV():
    archivo = open(f"{dniCliente}_AT_{datetime.today().strftime('%Y-%m-%d')}.csv", "w", newline='')
    spamreader = csv.writer(archivo)
    spamreader.writerow(archivoCSV)
    archivo.close()   

#Defino un objeto para saber cual es el cheque que mas se repite
def contarCheques(lista):
    return {i:numerosCheques.count(i) for i in numerosCheques}
#Cheques repetidos
cheques=contarCheques(numerosCheques)
maximo=max(cheques, key=cheques.get)

#aplico los condicionales para las impresiones
if opcion==1:
    #condicional para saber si existen mas de dos
    if cheques[maximo]==1:
        impresionPantalla()
    else:
        print("ERROR: Existen mas de dos cheques identicos")
elif opcion==2:    
    impresionCSV()
 

