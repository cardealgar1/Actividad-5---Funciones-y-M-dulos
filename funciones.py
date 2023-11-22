# capitulo 10 - página 204

# user functions
def sumar(i, j):  # parametro de entrada - input
    return i + j  # salida - output
suma_anonima= lambda i,j:i+j
print(f"el total de la suma anonima con lambda es {suma_anonima}")

def sumar_default(i, j, k=15):
    return i + j + k


def sumar_variable(*args):  # variable arguments
    total = 0
    for i in args:
        total += i
    return total


suma = sumar(4, 5)  # llamda a la funcion
print(f"el total de la suma es {suma}")

suma2 = sumar_default(4, 5)
print(f"el total de la suma con argmentos default es {suma2}")

suma3 = sumar_variable(5, 9, 4, 7)
print(f"la suma total de una funcion con argumentos variables es {suma3}")

#recursividad: una funcion se llama a si misma

def factorial(n):
    if n==1:
        return n
    elif n<=0:
        print("No hay factorial para 0 o menor que 0")
    else:
        return n*factorial(n-1) #recursividad porque se llama a si misma
resultado_factorial=factorial(6)
print(f"el factorial es {resultado_factorial}")