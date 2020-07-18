#Programa que el usuario ingresa una entrada para poder adivinar el numero_secreto que es generado aleatoriamente por la computadora.
#Importamos los modulos
import simplegui
import random
import math
#Definimos las variable globales
#Variable global para el numero generado aleatoriamente por la computadora
numero_secreto=0
#variable global que pone el rango de inicio por defecto
rango=100
#Variable global para la entrada del numero propuesto
entrada=0
#Variable que cuenta los intentos
n=0
#definiendo funciones de ayuda
def nuevo_juego():
    global numero_secreto,n
    numero_secreto=random.randint(0,rango)
    n=int(math.log(numero_secreto,2)+1)
    print "Nuevo juego, el rango es de 0 a", rango
    print "Te quedan",n,"intentos\n" 
#Constructor que cambia el rango a 100 y reinicia el juego
def rango100():
    global rango
    rango=100
    nuevo_juego()
#Constructor que cambia el rango a 1000 y reinica el juego
def rango1000():
    global rango
    rango=1000
    nuevo_juego()
#Funcion que se encarga de la logica del juego, donde recibe
#como parametro el numero ingresado para adivinarlo
def entrada_adivinar(adivina):
    global n,entrada
    entrada=int(adivina)
    #Condicional que verifica que los intentos no se hayan terminado
    if(n!=0):
        print ""
        #Muestra el numero que ingresó el usuario
        print "Ingresaste: ",entrada
        #Si n (los intentos) no es igual a 0 empieza a
        #verificar los casos 
        #Si entrada es mayor o menor al rango no le quita ninguna vida
        if(entrada>=rango or entrada<0):
            print "Numero fuera de limite"
            print "Te quedan",n," intentos"
        #Si entrada es menor que el numero_secreto imprime mas alto y quita una vida
        elif(entrada<numero_secreto):
            print "Mas alto"
            n-=1
            print "Te quedan",n," intentos"
        #Si entrada es mayor al numero secreto reduce una vida
        elif(entrada>numero_secreto):
            print "Mas bajo"
            n-=1
            print "Te quedan",n," intentos"
        #Si no es ninguno de los casos anteriores significa que el jugador ganó.
        else:
            print "HAS GANADO"
            print "Te quedaban",n," intentos"
            print ""
            nuevo_juego()
    #Si n==0 entonces el jugador ya perdió y vuelve a iniciar en el mismo rango 
        if n==0:
            print ""
            print "No te quedan mas intentos has perdido!"
            print ""
            nuevo_juego()
#Empezamos el juego con el rango inicial de 100
nuevo_juego()
#Creacion del frame y los botones
marco=simplegui.create_frame("ADIVINA EL NUMERO",200,300)
marco.add_input("Adivina el numero", entrada_adivinar,200)
marco.add_button("Rango 100", rango100,100)
marco.add_button("Rango 1000", rango1000,100)
#Iniciamos todo
marco.start()