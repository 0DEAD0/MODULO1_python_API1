from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "status": 200,
        "description": "tamos ready",
        "body": {}
    }

@app.get("/params")
def params(number: int = 666):

    lista =["mario", "pedro", "luis", "camila", "rosa"]

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

