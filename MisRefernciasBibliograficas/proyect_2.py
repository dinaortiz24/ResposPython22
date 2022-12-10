import mysql
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import matplotlib
#matplotlib.use('Agg')

db_host = 'localhost'
db_user = 'root'
db_pasw = '#Lys122620#'
db_name = 'db_macci'
db_port = 3306

# ---------- Estableciendo la conexión ---------
try:
    
    conn = mysql.connector.connect(
        user = db_user,
        password = db_pasw, 
        database = db_name,
        port = db_port, 
        host = db_host
        )
except:
    print("Falló la conexion")
# ---------------- Menú principal --------------
print ("========== Referencias Bibliograficas ========== \n")
print(" 1. Consultar Bibligrafia. \n 2. Salir  " )
menu = int (input ("\n Digite la opcion deseada: "))
    

#----------- Función Agregar --------    

def Agregar(titulo, autor, ubi, tipo, compa,ref,obs):
    
    
    query='INSERT INTO referencias (Ref, Titulo, Autor, Ubicacion, Tipo, compatibilidad,observ)VALUES("'+ref+'","'+titulo+'","'+autor+'","'+ubi+'","'+tipo+'",'+str(compa)+',"'+obs+'");'
    #print (query)
    
    #------------ ejecutador de la sencencia----------- 

    cursor = conn.cursor()
    cursor.execute(query)
    
    # ----------- Se aceptan los cambios ------------
    conn.commit()
    return
    conn.close
    
    #----------- Función Modificar -------- 
def modificar(titulo, autor, ubi, tipo, comp, in_ref,obs):
    
    query='UPDATE referencias SET Titulo = "'+titulo+'", Autor = "'+autor+'", Ubicacion = "'+ubi+'", Tipo= "'+tipo+'", compatibilidad ='+str(comp) +',observ="'+obs+'" WHERE (Ref="'+in_ref+'");'
   #print (query)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return
    conn.close
    
    
    #----------- Función Eliminar -------- 
def eliminar(in_ref):
    
    query='Delete from referencias  WHERE (Ref="'+in_ref+'");'
    #print (query)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return
    conn.close


#----------- Función Grafica -------- 
def grafica():
    query_graf='Select Ref, Titulo, compatibilidad from referencias order by Ref asc'
    cursor=conn.cursor()
    cursor.execute(query_graf)
    datos=cursor.fetchall()
    
    ref=[]
    comp=[]
    
    for row in datos:
        ref.append((row[0]))
        comp.append(row[2])
    fig, ax = plt.subplots()
    ax.bar(ref,comp)
    ax.set_ylabel('Porcentaje de compatibilidad')
    ax.set_title('Nivel de compatibilidad de referencia')
    plt.show()    
    return


#----------- Función Consulta General -------- 
def consulta():
 
    query_graf='Select Ref,Titulo, Autor,Ubicacion, Titulo,Tipo, compatibilidad, observ from referencias order by Ref asc'
    cursor=conn.cursor()
    cursor.execute(query_graf)
    datos=cursor.fetchall()
    
    ref=[]
    comp=[]
    tit=[]
    aut = []
    obs = []
    ubic = []
    tipo = []
    
    
    for row in datos:
        ref.append((row[1]))
        tit.append((row[2]))
        comp.append((row[6]))
        aut.append((row[3]))
        tipo.append((row[5]))
        ubic.append((row[4]))
        obs.append((row[7]))
        
    df = pd.DataFrame({'colum1':ref,'colum2':tit,'colum3':aut,'colum4':ubic,'colum5':tipo,'colum6':comp,'colum7':obs})
    df.columns= ['Numero de REF','Titulo','Autor','Ubicacion','Tipo','Compatibilidad','Observaciones']
    print(df)
    print()
    print('-----------------------------------------------------------------------------------')

    print('4.- Regresar al Menu \n') 
    print('5.- Agregar \n')  
    print('6.- Modificacion/Actualizacion \n')
    print('7.- Eliminacion  \n')
    print('8.- Graficar Compatibiidad\n')
    selec = int (input ("\n Digite la opcion deseada: "))
    if selec == 4:
       return consulta()
    
    #Modificar
    
    if selec == 6:         
         in_ref = (input ("\n referencia a modificar: "))
         tit = (input ("Ingrese el Titulo del documento \n "))
         aut = (input ("Ingrese el nombre del autor: \n "))
         ub = (input ("Ingrese la ubicacion del archivo:  \n "))
         tip = (input ("Ingrese el tipo de documento: \n "))
         comp = int (input ("\n Ingrese la compatibilidad con su tema: \n"))
         obs = (input ("\n Ingrese sus observaciones: \n"))
         
         modificar(tit,aut,ub,tip,comp,in_ref,obs)
         #print(" \n 4.- Regresar al menu principal . \n 2.- Salir  " )
         #menu = int (input ("\n Digite la opcion deseada: "))
         
         #eliminar
         
    if selec==7:
        in_ref = (input ("\n Referencia a Eliminar: "))
        eliminar(in_ref)
        
    if selec==8:
        grafica()
        
        #Agregar
    if selec == 5:
            print ('Ingrese los datos\n' )
            tit = (input ("Ingrese el Titulo del documento \n "))
            aut = (input ("Ingrese el nombre del autor: \n "))
            ub = (input ("Ingrese la ubicacion del archivo:  \n "))
            tip = (input ("Ingrese el tipo de documento: \n "))
            comp = int (input ("\n Ingrese la compatibilidad con su tema: \n"))
            obs = (input ("\n Ingrese sus observaciones: \n"))           
            ref =( (input ("\n Ingrese la referencia: \n")))        
            Agregar(tit,aut,ub,tip,comp,ref,obs)
           
 #----------- ciclo para permanecer en menu -------- 
#try:
while menu!=0:
    if menu == 4:
        print ("\n  ========== Referencias Bibliograficas ========== \n")
        print(" 1.- Consultar Bibligrafia. \n 2.- Salir  " )
        menu = int (input ("\n Digite la opcion deseada: "))
   
    if menu == 1:
        consulta()
        print(" 4. Regresar al menu principal . \n 2. Salir  " )
        menu= int (input ("\n Digite la opcion deseada: "))
   
    if menu == 2:
        conn.close
        menu = 0
        exit
#except:
 #   print("Algo salio mal, intente mas tarde")
  #  exit
    