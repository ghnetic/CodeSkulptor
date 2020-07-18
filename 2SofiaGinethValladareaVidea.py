#Juego piedra, papel, tijera, lagarto, spock
#Importamos random para la seleccion aleatoria de la computadora
import random
#Funcion para convertir el nombre a numero
def nombre_a_numero(nombre):
    if nombre=="piedra":
        opcionNombre=0
    elif nombre=="papel":
        opcionNombre=1
    elif nombre=="tijera":
        opcionNombre=2
    elif nombre=="lagarto":
        opcionNombre=3
    else:
        opcionNombre=4
    return opcionNombre

#Funcion para convertir el numero a nombre
def numero_a_nombre(numero):
    if numero==0:
        opcionNumero="piedra"
    elif numero==1:
        opcionNumero="papel"
    elif numero==2:
        opcionNumero="tijera"
    elif numero==3:
        opcionNumero="lagarto"
    else:
        opcionNumero="spock"  
    return opcionNumero

#Funcion que contiene la logica del juego
def pptls(eleccion_jugador):
    computadora=numero_a_nombre(random.randrange(0, 4))
    jugador=nombre_a_numero(eleccion_jugador)
    
    print "El jugador eligio" , numero_a_nombre(jugador)
    print "La computadora eligio", computadora
    
    #Verifica primero si es un empate
    if computadora==numero_a_nombre(jugador):
        print "Es un empate"
    
    #Sino sigue verificando las demas opciones
    #Opciones de Piedra
    elif computadora=="piedra":
        if jugador==2 or jugador==3:
            print "Gana Computadora!"
        else:
            print "Gana Jugador!"
    #Opciones de Papel       
    elif computadora=="papel":
        if jugador==0 or jugador==4:
            print "Gana Computadora!"
        else:
            print "Gana Jugador!"
    #Opciones de Tijera      
    elif computadora=="tijera":
        if jugador==1 or jugador==3:
            print "Gana Computadora!"
        else:
            print "Gana Jugador!"
    #Opciones de Lagarto
    elif computadora=="lagarto":
        if jugador==4 or jugador==1:
            print "Gana Computadora!"
        else:
            print "Gana Jugador!"
    #Opciones de Spock
    elif computadora=="spock":
        if jugador==2 or jugador==0:
            print "Gana Computadora!"
        else:
            print "Gana Jugador!"
            
    print ""
    
#Escribimos las opciones del jugador      
pptls("piedra")
pptls("papel")
pptls("tijera")
pptls("lagarto")
pptls("spock")