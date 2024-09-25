# Almacenar un número secreto
numero_secreto = 4  # es un numero de ejemplo,puedes cambiar este número
# Inicializar la variable para el intento del usuario
intento = None
# Bucle para pedir al usuario que adivine
while intento != numero_secreto:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")
print("")
print("mejia suarez emmanuel alexander:mi practica es de asignacion de variables")
print("")
