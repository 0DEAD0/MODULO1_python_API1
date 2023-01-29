from fastapi import FastAPI

app = FastAPI()
lista =["mario", "pedro", "luis", "camila", "rosa"]

@app.get("/")
def health():
    return {
        "status": 200,
        "description": "tamos ready",
        "body": {}
    }

@app.get("/params")
def params(number: int = 666):
    global lista
    
    try:
        response = lista[number]
        satatus = 200
        description = ""
    except IndexError:
        response = ""
        status = 400
        description = "No existe estudiantes en esa posicion"

    return {
        "status": 200,
        "description":"",
        "body": {"number": response
        }
    }

@app.post("/inputparameter")
def input_param(body_request: dict):
    global lista

    try:
       lista.append(body_request["new_student"])
       status= 200
       description = ""
       add = "ok"
    except KeyError:
        response = "",
        status = 400
        description = "la llave del body request es incorrecta, debe ser new_student"
        add = "Fail"
    return{
        "status": status,
        "description": description,
        "body": {
            "add": add
        }
    }