#vamos a utilizar el contenido del modulo 2

import ejemplo2
from ejemplo3 import Pais

#uso de variables
ejemplo2.alumno.update({'luis': 'dam'})
print(ejemplo2.alumno)

#uso de funciones
ejemplo2.calcular_cubo()

#uso de una clase
producto1=ejemplo2.Producto('camisa',50)

francia=Pais("France", "Paris")