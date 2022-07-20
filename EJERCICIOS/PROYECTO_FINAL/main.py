"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random # importa una serie de numeros aleatorios
import string # importa una cadena
from palabras import palabras #se define como una variable palabras y se importa el archivo palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras):#para seleccionar al azar palabra y toma la palabra 
    palabra = random.choice(palabras)# se escoge la palabra 


    while '-' in palabra or ' ' in palabra:#se hace un ciclo hasta que se cumpla la condicion
        palabra = random.choice(palabras)#buscar la palabra

    return palabra.upper()#se regresa palabra en mayusculas


def ahorcado():# define una funcion con el nombre del juego

    print("=======================================")#hace caja para hacer la bienvenida al juego para mostrarla 
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)# definir una funcion con palabra, para hacer una lista de palabras se crea un archivo y se importa
    letras_por_adivinar = set(palabra)# se crea variable con un conjunto de letras
    abecedario = set(string.ascii_uppercase) # se crea otra valiable con cadenas y letras mayusculas del abecedario
    letras_adivinadas = set() #se crea tambien esta otra variable 

    vidas = 7 #se crea variable de vidas


    while len(letras_por_adivinar) > 0 and vidas > 0:#se crea este ciclo no se sabe cuantas repeticiones se van a dar

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")# imprime las vidas que te quedan y usando un metodo join

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]# muestra si la letra se encuentra en la palabra
        print(vidas_diccionario_visual[vidas])# imprime las vidas que quedan y se toma del diccionario visual 
        print(f"Palabra: {' '.join(palabra_lista)}") #muestra la palabra como se encuentra 

     
        letra_usuario = input('Escoge una letra: ').upper()#se hace otra variable para ingresar una letra en mayuscula

        if letra_usuario in abecedario - letras_adivinadas:#condicional si esta la letra en el abecedario
            letras_adivinadas.add(letra_usuario)#se adiciona la letra que se ingreso, se incluye en las letras ingresadas
       
            if letra_usuario in letras_por_adivinar:#si no esta la letra en la palabra
                letras_por_adivinar.remove(letra_usuario)# se le quita la letra
                print('')
         
            else:
                vidas = vidas - 1 #si no se le disminuye una vida
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")#si no imprime ya escoge una letra nueva
        else:
            print("\nEsta letra no es válida.")#no esta letra no es valida

   
    if vidas == 0:# cuando ya no tiene vida o sea 0 vidas, o gano
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")# se imprime lo lamento
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')#o el jugador ha ganado

if__name__=='__main__':#esta condicion falta, ya que no corre 
    
    ahorcado()# se inicia el juego
