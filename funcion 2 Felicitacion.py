### Program created by Jessi
### Date: 20/10/2025
### Definición de funciones Felicitación

def examen ():
    puntos=0
    #Pregunta 1
    xxx = input ("El comando COPY en Windows sirve para copiar archivos. (V/F)?: ")
    if xxx=="V":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif

    #Pregunta 2
    xxx = input ("El comando DIR sirve para mover o renombrar archivos. (V/F)?: ")
    if xxx=="F":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif
    print("Tu nota final es:")
    print(puntos)

def felicitacion():
    print("Felicitaciones, siga estudiando así.")
    print("Estamos orgullosos de usted")

##### Main Program
xname = input("Dime tu nombre, por favor:")
print("Hola, " + xname + "!")
a="Vamos a hacer un test de dos preguntas sobre"
b=" Microsoft Windows."
print(a+b)
examen()
felicitacion()
print("Fin de la prueba.")