from fastapi import FastAPI
from typing import Optional
import uvicorn
from db import engine,connection_db,conn
from sqlalchemy import func, select

"""app = FastAPI()
from models import *
@app.get('/hello')
def hello():
    return {"respuesta":'hola'}

@app.get('/datos_faker')
def datos():
    a = conn.execute(datos_falsos.select()).fetchall()
    return {"respuesta":a}

@app.get('/insert_data')
def insert_data():
    new_data = {"name": "pacho", "email": "pacho@gmail.com"}
    result = conn.execute(datos_falsos.insert().values(new_data))
    return {"respuesta":"asdasdasd"} """
app = FastAPI()

from models import *
@app.route('/crear_registros')
def crear_registros():
    url = 'http://faker-service/datos'
    response = requests.get(url)
    response_json = json.loads(response.text)
    for i in response_json["datos"]:
        data = DataFaker(nombre=i["name"],ciudad=i["city"],direccion=i["address"],telefono=i["phone_number"])
        db.session.add(data)
    db.session.commit()
    return {'data':"Registros creados"}

@app.route('/registros_faker')
def registros_faker():
    with engine.connect() as con:
        obtener_data = "select * from datos_falsos"
        respuesta_data = con.execute(obtener_data)
        lista = list()
        for i in respuesta_data:
            data = dict()
            data["name"] = i[1]
            data["ciudad"] = i[3]
            data["direccion"] = i[4]
            data["telefono"] = i[5]
            lista.append(data)
        return {'data':lista}

