"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random # importa una serie de numeros aleatorios
import string # importa una cadena
from palabras import palabras #se define 
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras):#para seleccionar al azar palabra 
    palabra = random.choice(palabras) 


    while '-' in palabra or ' ' in palabra:#se hace un ciclo hasta que se cumpla la condicion
        palabra = random.choice(palabras)#buscar la palabra

    return palabra.upper()#palabra en mayusculas


def ahorcado():# define una funcion el nombre

    print("=======================================")#hace caja para hacer la bienvenida al juego para mostrarla 
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)# definir una funcion con palabra, para hacer una lista de palabras
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase) 
    letras_adivinadas = set()  

    vidas = 7


    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
       
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

   
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado()
