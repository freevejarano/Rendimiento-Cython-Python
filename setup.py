'''
    EJERCICIO DE RENDIMIENTO CYTHON/PYTHON
    Autor: Luis Alejandro Vejarano Gutierrez
    Clase: Computación Paralela y Distribuida
    Universidad Sergio Arboleda 06/05/2021
'''

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ext = Extension(name = 'CyFunctionE',sources=['CyFunctionE.pyx'])

setup(ext_modules=cythonize(ext,
        compiler_directives={'language_level': 3}),
        include_dirs=[numpy.get_include()])