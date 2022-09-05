#python listado_cheques.py cuentas.csv 1617591371 CVS EMITIDO APROBADO 12-05-2000:25-05-2000
import sys
import csv
from datetime import datetime

#Parametros
nomb_csv=sys.argv[1]
dni_cliente=sys.argv[2]
salida=sys.argv[3]


entrada=""
listaUsuario=[] 
 
#Guarda archivos csv
archivoCSV=[]  
archivoCSV.append("NumeroCuentaDestino,Valor,FechaOrigen,FechaPago\n")

#Numeros de cheques
numerosCheques=[]

#Abre archivo csv 
with open(nomb_csv) as File:
    reader = csv.DictReader(File)
    #Bucle para recorrer el csv
    for row in reader:
        listaUsuario.append(row)

#Filtra el dni ingresado
usuario=(list(filter(lambda item: item['DNI'] == dni_cliente, listaUsuario)))

#fecha y numero de cheque
for i in usuario:
    datos= usuario
    origen=int(i['FechaOrigen'])
    pago=int(i['FechaPago'])
    origen= str(datetime.fromtimestamp(origen))
    pago=str(datetime.fromtimestamp(pago))
    num=int(i['NroCheque'])
    numerosCheques.append(num)
    archivoCSV.append(i['NumeroCuentaDestino']+i['Valor']+origen+pago+"\n")


#Defino un objeto para saber cual es el cheque que mas se repite
def contarCheques(lista):
    return {i:numerosCheques.count(i) for i in numerosCheques}
#Cheques repetidos
cheques=contarCheques(numerosCheques)
maximo=max(cheques, key=cheques.get)


#condicional para saber si existen mas de dos cheques
if cheques[maximo]!=1:
    print("ERROR: Existen mas de dos cheques identicos")
    
if cheques[maximo]==0:
    print("ERROR: No existen cheques")
    


#Salidas    
if salida== "CSV" or salida== "csv":
    archivo = open(f"{dni_cliente}_AT_{datetime.today().strftime('%Y-%m-%d')}.csv", "w", newline='')
    spamreader = csv.writer(archivo)
    spamreader.writerow(archivoCSV)
    archivo.close()   

if salida== "PANTALLA" or salida== "pantalla":
    for i in usuario:
        print("Usuario: "+i['DNI']+" Nro de cheque: "+i['NroCheque']+" Tipo de cheque: "+i['Tipo']+" Estado del cheque: "+i['Estado'])
      
#Filtrado de cheques
#filtrados por el estado depositado o emitido
cheque_filtrado = []
# Los cheques filtrados por el estado 
cheque_estado = []  

stdo_cheque=sys.argv[4]
rango_fecha=sys.argv[6]



print(usuario)
print(stdo_cheque,cheque_filtrado)



