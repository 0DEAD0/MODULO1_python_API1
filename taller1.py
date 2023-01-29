from fastapi import FastAPI

app = FastAPI()

#configuracion de el man esta vivo 
@app.get("/")
async def health():
    return {
        "status":200,
        "description": "Estoy vivo",
        "body": {}
    }


#segundo punto, lee la database y retorna las ciudades 
@app.get("/2")
async def segundo_punto():
#variables auxiliares
    datos = []
    pais_list= []
    ciudad_list = []
    pais = 0
#lee el documento 
    with open("database.txt","r") as fname:
        lineas = fname.readlines()
#divide las lineas para almacenamiento 
        for linea in lineas:
            datos.append(linea.strip('\n'))
#almacena las ciudades y paises 
        for line in datos :
            pais_list.append(line[line.find(",")+2:line.rfind(",")])
            ciudad_list.append(line[line.rfind(",")+2:])
#retorna las ciudades 
    return {
        "status":200,
        "description": "",
        "body": {
            "ciudades":ciudad_list
        }
    }
#tercer punto 
@app.get("/3")
async def tercer_punto(ciudad:str):
    datos = []
    pais_list= []
    ciudad_list = []
    pais = 0

    with open("database.txt","r") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))

        for line in datos :
            pais_list.append(line[line.find(",")+2:line.rfind(",")])
            ciudad_list.append(line[line.rfind(",")+2:])
    #se transforman todas las letras en minusculas 
    for it in ciudad_list:
        if (ciudad.lower() == it.lower()):
            aux = pais 
        pais +=1

    try:
        status= 200
        description= ""
        response = pais_list[aux]
        #si se escribe una ciudad fuera de la lista, la ciudad no existe, error 400
    except: 
        status=400
        description= "la ciudad no existe"
        response = ""


    return{
        "status": status,
        "description": description,
        "body":{
            "pais": response
        }
    }

    #cuarto punto 
@app.get("/4")
async def cuarto_punto(ids:int):
    datos = []
    pais_list= []
    ciudad_list = []
    pais = 0

    with open("database.txt","r") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))

        for line in datos :
            pais_list.append(line[line.find(",")+2:line.rfind(",")])
            ciudad_list.append(line[line.rfind(",")+2:])
    
#si se introduce una id no valida, entonces la id no existe
    try:
        status= 200
        description= ""
        response1 = pais_list[ids-1]
        response2 = ciudad_list[ids-1]
    except: 
        status=400
        description= "la id no existe"
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

#sexto punto 
@app.get("/6")
async def punto6(ids:int):
    try:
        with open("database.txt", "r") as fr:
            p = fr.readlines()
            ptr = 1
            with open("database.txt", "w") as fw:
                for j in p:
                    if ptr != ids:
                        fw.write(j)
                    ptr += 1
        status = 200
        description = ""
#se elimina la linea elegida ingresando la id
    except:
        status = 400
        description = "la id no existe"
    


    return {
        "status": status,
        "description": description,
        "body":{}
    }