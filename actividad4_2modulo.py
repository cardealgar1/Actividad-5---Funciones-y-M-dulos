from simulacion import Silla, Color

try:
    silla_azul = Silla(Color.AZUL, 9.95)
    silla_roja = Silla(Color.ROJA, 9.95)

    print(f"Silla azul - Color: {silla_azul.color.value}, Precio: {silla_azul.precio}€")
    print(f"Silla roja - Color: {silla_roja.color.value}, Precio: {silla_roja.precio}€")

except Exception as e:
    print(f"Error: {e}")
