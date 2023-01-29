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