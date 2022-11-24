import csv
import random as rd
import interfaz


def leer_palabra_secreta(csvfilename):
    with open(csvfilename) as archivo:
        lista_palabras_secretas = list(csv.DictReader(archivo))
        palabra_secreta = rd.choice(lista_palabras_secretas)
        return palabra_secreta['palabras']


def pedir_letra(letras_usadas):
    while True:
        letra_ingresada = (input('ingresa una letra del alfabeto: ')).lower()
        # evaluamos si el dato ingresado no es una letra del alfabeto
        if not letra_ingresada.isalpha():
            print('debes ingresar una letra del alfabeto, intenta de nuevo...\n')
        # evaluamos si el dato ingresado es de una sola letra
        elif len(letra_ingresada) > 1:
            print('debes ingresar una sola letra, intenta de nuevo...\n')
        # evaluamos si la letra no se habia utilizado con anterioridad
        elif letra_ingresada in letras_usadas:
            print('letra ya utilizada, intenta de nuevo...\n')
        # si el flujo llega acá la letra esta validada
        else:
            return letra_ingresada


def verificar_letra(letra, palabra_secreta):
    return letra in palabra_secreta


def validar_palabra(letras_usadas, palabra_secreta):
    cantidad_letras = len(palabra_secreta)

    for index in range(len(letras_usadas)):
        cantidad_letras -= palabra_secreta.count(letras_usadas[index])
        if cantidad_letras == 0: return True
        else: return False

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')

    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # decido agregar la letra validada en esta parte del programa y no en
        # la función pedir_letra() debedio al alcace local de la variable
        # letras_usadas

        letras_usadas.append(letra)

        # Verificar si la letra es parte de la palabra secreta
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1

        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(
            f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(
            f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')
