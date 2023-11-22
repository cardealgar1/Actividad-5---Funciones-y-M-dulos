'''Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''


def suma_numeros():
    numeros = []

    for _ in range(5):
        while True:
            entrada = input(f"Introduce el {len(numeros) + 1}º número (o 'q' para salir): ")

            if entrada.lower() == 'q':
                break

            try:
                numero = float(entrada)
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Ingresa un número válido.")

    suma = sum(numeros)
    return suma

resultado = suma_numeros()
print(f"La suma de los números introducidos es: {resultado}")



'''Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''

from datetime import datetime

def calcular_subtotal(unidades, precio):
    return unidades * precio

def aplicar_descuento(subtotal, fecha):
    dia_actual = fecha.day
    if dia_actual < 15:
        return subtotal * 0.95
    else:
        return subtotal

def obtener_datos():
    try:
        unidades = int(input("Ingrese la cantidad de unidades: "))
        precio = float(input("Ingrese el precio por unidad: "))
        return unidades, precio
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return obtener_datos()

def main():
    try:
        unidades, precio = obtener_datos()
        subtotal = calcular_subtotal(unidades, precio)
        fecha_actual = datetime.now()
        total = aplicar_descuento(subtotal, fecha_actual)
        print(f"\nSubtotal: {subtotal:.2f}€")
        print(f"Total con descuento: {total:.2f}€")
    except Exception as e:
        print(f"Error inesperado: {e}")

main()


'''Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''

def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingresa un número válido.")

def obtener_numeros_pares(inicial, final):
    return list(filter(lambda x: x % 2 == 0, range(inicial, final + 1)))

def main():
    try:
        inicial = obtener_numero("Ingresa el número inicial: ")
        final = obtener_numero("Ingresa el número final: ")

        if inicial > final:
            print("Error: El número inicial debe ser menor o igual al número final.")
            return

        numeros_pares = obtener_numeros_pares(inicial, final)

        if numeros_pares:
            print("Números pares entre {} y {}: {}".format(inicial, final, numeros_pares))
        else:
            print("No hay números pares en el rango proporcionado.")

    except Exception as e:
        print("Error inesperado:", e)
main()

'''Actividad 4
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''

from enum import Enum

class Color(Enum):
    AZUL = "azul"
    ROJA = "roja"

class Mueble:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Mesa(Mueble):
    def __init__(self, color, precio):
        super().__init__(color, precio)

class Silla(Mueble):
    def __init__(self, color, precio):
        super().__init__(color, precio)

class Lampara(Mueble):
    def __init__(self, color, precio):
        super().__init__(color, precio)
