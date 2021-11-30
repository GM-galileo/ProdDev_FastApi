#Gabriela Mazariegos

from fastapi import FastAPI, Response
from fastapi import FastAPI, Query
from typing import List, Optional
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Tarea - FastApi"}


@app.get("/suma/")
def suma_arreglo(arregloS: List[int] = Query(None)):
    suma_arr = np.sum(np.array(arregloS))
    return {'Total Suma: ': suma_arr.tolist()}

@app.get("/resta/")
def resta_arreglo(arregloR: List[int] = Query(None)):
    res_arr = np.diff(np.array(arregloR))
    return {'Total Resta: ': res_arr.tolist()}

@app.get("/multiplicacion/")
def multi_arreglo(arregloM: List[int] = Query(None)):
    mul_arr = np.prod(arregloM)
    return {'Total Multiplicacion: ': mul_arr.tolist()}

@app.get("/division/")
def div_arreglo(arregloD: List[int] = Query(None)):
    arr2 = arregloD[1:]
    arr3 = np.append(arr2, 1)
    div_arr = np.divide(arregloD, arr3)[:-1]
    return {'Total Division: ': div_arr.tolist()}


@app.get("/operaciones/{operacion}/arreglo/")
def Operacion_arreglo(operacion: str, arregloO: List[int] = Query(None)):

    op = np.array([])
    if (operacion == "suma"):
        op = np.sum(np.array(arregloO))
    elif  (operacion == "resta"):
        op = np.diff(np.array(arregloO))
    elif (operacion == "multiplicacion"):
        op = np.prod(arregloO)
    elif (operacion == "division"):
        arr2 = arregloO[1:]
        arr3 = np.append(arr2, 1)
        op = np.divide(arregloO, arr3)[:-1]

    return {'Total Operacion: ': op.tolist()}
