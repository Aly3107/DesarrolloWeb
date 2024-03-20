import Proyecto_Python.Categorias as Categorias
import random

palabras = Categorias.categorias

def seleccionar_categoria(palabras):
    print("Seleccione una categoría: ")
    while True:
        print("""
        1, Animales acuaticos
        2, Animales terrestres
        3, Dinosaurios
        4, Películas animadas de Disney
        """)
        categoria_seleccionada = input("Seleccione el número de acuerdo a la categoría: ")
        if categoria_seleccionada == "1":
            palabra_secreta = random.choices(palabras["Animales_acuaticos"])
            return palabra_secreta

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

palabra_secreta = seleccionar_categoria(palabras)

print(palabra_secreta)