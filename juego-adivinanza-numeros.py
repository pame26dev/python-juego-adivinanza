import random


def juego_adivinanza():
    # Generar un numero secreto del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinando = False

    # Primeras lineas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 y el 100")
    print("¡Intenta adivinarlo!")

    while not adivinando:
        # Solicitar el numero del 1 al 100
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        # Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # lo estamos pasando de texto a numero
            intentos += 1
            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos}."
                )
        else:
            print("Por favor introduzca un número válido entre 1 y 100")


juego_adivinanza()
