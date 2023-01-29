from fastapi import FastAPI

app = FastAPI()

#solocitud get para dar aviso que la aplicacion esta funcionando correctamente
@app.get("/")
async def health():
    return {
        "status":200,
        "description": "Estoy vivo",
        "body": {}
    }


#segundo punto, lee la database y mostrar solo las ciudades
@app.get("/ciudades")

async def ciudades():

#variables
    lista_paises= []
    lista_ciudades = []
    datos = []

#cargar base de datos
    with open("database.txt","r") as file:
        base_datos = file.readlines()

#separando las lines para guardarlas en orden
        for linea in base_datos:
            datos.append(linea.strip('\n'))

#guardando ciudades y paises en las variables anteriormente creadas  
        for linea in datos :                                               #ciclo for para recorrer las listas de manera dinamica e ir reemplazando los valores
            lista_paises.append(linea[linea.find(",")+2:linea.rfind(",")])  #se usa rfine para encontras la ultima aparicion de el valor guardado
            lista_ciudades.append(linea[linea.rfind(",")+2:])

#mostrando las ciudades
    return {
        "status":200,
        "description": " ",
        "body": {
            "ciudades":lista_ciudades
        }
    }

#punto 3 digitar ciudad y devolver pais
@app.get("/Digite una ciudad para saber su pais")
async def ciudad_pais(ciudad:str):


    lista_paises= []
    lista_ciudades = []
    datos = []
    contador = 0

    with open("database.txt","r") as file:
        base_datos = file.readlines()
        file.close()
    
        for i in base_datos:
            datos.append(i.strip('\n'))  # se usa el ciclo for con la funcion strip para eliminar para eliminar los espacios de inicio en cada linea y guardas todos los datos en la lista datos

        for linea in datos :                                                #ciclo for para recorrer las listas de manera dinamica e ir reemplazando los valores
            lista_paises.append(linea[linea.find(",")+2:linea.rfind(",")])  #se usa rfine para encontras la ultima aparicion de el valor guardado
            lista_ciudades.append(linea[linea.rfind(",")+2:])

    
    for letras in lista_ciudades:              # en este for tomamos todos los datos y con la funcion lower los pasamos a minusculas 

        if (ciudad.lower() == letras.lower()): #para que asi siempre podamos encontrar las ciudades dentro del condicionalo if con un contador que buscara dentro de la lista de uno en uno
            aux = contador                          
        contador +=1

    try:
        status= 200
        description= ""
        response = lista_paises[aux]
                                       # si el usuario ingresa una ciudad que no esta en la lista automaticamente le saldra el error
    except: 
        status=400
        description= "la ciudad no se encuentra en la lista"
        response = ""

    return{
        "status": status,
        "description": description,
        "body":{
            "pais": response
        }
    }

    # Que permita obtener el país y la ciudad cuando se pase un id
@app.get("/Digite el numero el cual desea saber la ciudad y pais segun la lista inicial")

async def pais_ciudad(id:int):

    lista_paises= []
    lista_ciudades = []
    datos = []

    with open("database.txt","r") as file:
        base_datos = file.readlines()
        file.close()
    
        for i in base_datos:
            datos.append(i.strip('\n'))  # se usa el ciclo for con la funcion strip para eliminar para eliminar los espacios de inicio en cada linea y guardas todos los datos en la lista datos

        for linea in datos :                                                #ciclo for para recorrer las listas de manera dinamica e ir reemplazando los valores
            lista_paises.append(linea[linea.find(",")+2:linea.rfind(",")])  #se usa rfine para encontras la ultima aparicion de el valor guardado
            lista_ciudades.append(linea[linea.rfind(",")+2:])
    
                         #si el usuario pone una id que no esta en nuestra lista le manda error de ciudad no valida
    try:
        status= 200
        description= ""
        response1 = lista_paises[id-1]
        response2 = lista_ciudades[id-1]
    except: 
        status=400
        description= "la id no se encuentra en la lista"
        response1 = ""
        response2 = ""


    return{
        "status": status,
        "description": description,
        "body":{
            "pais": response1,
            "ciudad": response2,
        }
    }

#  Que permita agregar una nueva ciudad y país con un Request Parameter.
#@app.post("/ingresa_ciudad_P/{nombre_pais}/{nombre_ciudad}")
#async def ingresa_ciudad_P/(nombre_pais)

#Que permita eliminar una ciudad y país, pasando su id con un Query Parameter

@app.get("/Digite el id de la ciudad que desea eliminar")

async def eliminar(id:int):
    try:
        
        with open("database.txt", "r") as file:
            base = file.readlines()
            sumador = 1
           
            with open("database.txt", "w") as files:     #aqui se abre la base de datos en modo escritura para poder cambiar la ide que se desea eliminar

                for linea in base:    
                                                #el cilo recorre la lista buscando el ingresado para luego con el condicional if se busca la linea deseada y la reemplaza con un espacio vacio
                    if sumador != id:               
                        files.write(linea)
                    sumador += 1
        status = 200
        description = ""                             
    except:
        status = 400
        description = "la id no se encuentra en la lista"
    return {
        "status": status,
        "description": description,
        "body":{}
    }
