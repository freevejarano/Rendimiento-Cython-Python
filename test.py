#!/usr/bin/python3
'''
    EJERCICIO DE RENDIMIENTO CYTHON/PYTHON
    Autor: Luis Alejandro Vejarano Gutierrez
    Clase: Computación Paralela y Distribuida
    Universidad Sergio Arboleda 06/05/2021
'''
from functionE import rbf_network
from CyFunctionE import Cy_rbf_network
import numpy as np
import time

# Inicialización de variables
Py_D = 5
Py_N = 1500
Py_X = np.array([np.random.rand(Py_N) for d in range(Py_D)]).T
Py_beta = np.random.rand(Py_N)
Py_theta = 10

# Listas de Ejecuciones 
pTiempoPy, pTiempoCy, pSpeedUp = [], [], []

# Para el test se repetirá n veces la toma de tiempos
n = 30
for i in range(n):
    inicio = time.time()
    rbf_network(Py_X, Py_beta, Py_theta)
    tiempoPy = time.time() - inicio
    pTiempoPy.append(tiempoPy)

    inicio = time.time()
    Cy_rbf_network(Py_X, Py_beta, Py_theta)
    tiempoCy = time.time() - inicio
    pTiempoCy.append(tiempoCy)

    speedUp = round(tiempoPy/tiempoCy,3)
    pSpeedUp.append(speedUp)

promPy = round(sum(pTiempoPy)/len(pTiempoPy),3)
promCy = round(sum(pTiempoCy)/len(pTiempoCy),3)
promSpeedUp = round(sum(pSpeedUp)/len(pSpeedUp),3)

print(f"Al ejecutar {n} veces:\n")
print(f"Tiempo promedio Python: {promPy}")
print(f"Tiempo promedio Cython: {promCy}")
print(f"Promedio SpeedUp: {promSpeedUp}")