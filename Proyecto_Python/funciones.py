import Proyecto_Python.Categorias as Categorias
import random

palabras = Categorias.categorias

def seleccionar_categoria(palabras):
    print("Seleccione una categoría: ")
    while True:
        print("""
        1. Animales del bosque
        2. Animales del desierto
        3. Animales de la selva
        4. Animales de la montaña
        5. Animales del océano
        6. Dinosaurios del périodo triásico
        7. Dinosaurios del périodo jurásico
        8. Dinosaurios del périodo cretácico
        9. Peliculas animadas de Disney
        10. Peliculas animadas de Pixar
        11. Peliculas animadas de Dreamworks
        """)
        categoria_seleccionada = input("Ingresa el número de acuerdo a la categoría: ")
        if categoria_seleccionada == "1":
            palabra_secreta = random.choices(palabras["Animales_bosque"])
            return palabra_secreta
        elif categoria_seleccionada == "2":
            palabra_secreta = random.choices(palabras["Animales_desierto"])
            return palabra_secreta
        elif categoria_seleccionada == "3":
            palabra_secreta = random.choices(palabras["Animales_selva"])
            return palabra_secreta
        elif categoria_seleccionada == "4":
            palabra_secreta = random.choices(palabras["Animales_montaña"])
            return palabra_secreta
        elif categoria_seleccionada == "5":
            palabra_secreta = random.choices(palabras["Animales_oceano"])
            return palabra_secreta
        elif categoria_seleccionada == "6":
            palabra_secreta = random.choices(palabras["Dinosaurios_triasico"])
            return palabra_secreta
        elif categoria_seleccionada == "7":
            palabra_secreta = random.choices(palabras["Dinosaurios_jurasico"])
            return palabra_secreta
        elif categoria_seleccionada == "8":
            palabra_secreta = random.choices(palabras["Dinosaurios_cretacico"])
            return palabra_secreta
        elif categoria_seleccionada == "9":
            palabra_secreta = random.choices(palabras["Peliculas_animadas_Disney"])
            return palabra_secreta
        elif categoria_seleccionada == "10":
            palabra_secreta = random.choices(palabras["Peliculas_animadas_Pixar"])
            return palabra_secreta
        elif categoria_seleccionada == "11":
            palabra_secreta = random.choices(palabras["Peliculas_animadas_Dreamworks"])
            return palabra_secreta
        else: 
            print("Número no valido, ingresa un número de acuerdo de su categoría")

def mostrar_palabra(palabra, letras_adivinadas):
    visualizacion = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            visualizacion += letra
        else:
            visualizacion += "_"
    return visualizacion

def letra_adivinada(palabra, letras_adivinadas):
    for letra in palabra:
        if letra not in letras_adivinadas:
            return False
    return True

def ahorcado():
    palabra_secreta = seleccionar_categoria(palabras)
    letras_adivinadas = []
    intentos = 8

print("¡Bienvenido al juego del Ahorcado!")
print(mostrar_palabra(palabra, letras_adivinadas))

while intentos >0:
    intento = input("Adivina una letra: ").lower()
    if intento in letras_adivinadas:
        print("¡Bien, adivinaste una letra!")
    elif intento in palabra_secreta:
        letras_adivinadas.append(intento)
        print("¡Vas bien!")
    else:
        intentos -= 1
        print(f"""
        ¡Letra incorrecta!, vuelve a intentarlo. 
        Tienes {intentos} restantes""")

    print(mostrar_palabra(palabra, letras_adivinadas))
    if letra_adivinada(palabra, letras_adivinadas):
        print("¡Felicidades!, haz adivinado la palabra.")
        break
    
if intentos == 0:
    print(f"¡Te has quedado sin intentos! La palabra secreta era: {palabra_secreta}")

print(palabra_secreta)