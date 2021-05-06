'''
    EJERCICIO DE RENDIMIENTO CYTHON/PYTHON
    Autor: Luis Alejandro Vejarano Gutierrez
    Clase: Computación Paralela y Distribuida
    Universidad Sergio Arboleda 06/05/2021
'''

#cython: language_level=3, boundscheck=False, wraparound=False, nonecheck=False

cimport cython
cdef extern from "math.h":
    long double exp(double x) nogil
import numpy as np
cimport numpy as np

def Cy_rbf_network(double[:, :]  X, double[:]  beta, double theta):

    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef double[:] Y = np.zeros(N)
    cdef int i
    cdef int j
    cdef int d
    cdef double r

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y