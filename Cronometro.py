#Programa que simula un cronometro 
#Importamos el modulo
import simplegui
#Definimos variables globales con letras mayusculas
CONTADOR = 0
ACERTADOS = 0
INTENTOS = 0
ANCHO=500
ALTO=500
CENTRO=[180,250]
SUPERIORDERECHA=[420,50]
       
#Funcion para detener el juego, y verifica si tiene un acierto o solamente un intento
def detener():
    global ACERTADOS,INTENTOS
    #Detenemos el temporizador
    temporizador.stop()
    #Verificamos si el modulo del contador es igual a 0 para comprobar si se detuvo en 1 minuto exactamente.
    if(CONTADOR%10==0):
        ACERTADOS+=1
        INTENTOS+=1
    #Aunque no acierte, se le suma un intento
    else:
        INTENTOS+=1
        
#Controlador que reanuda por donde se quedó al detenerse
def empezar():
    #verifica si el temporizador esta detenido
    if not temporizador.is_running():
        temporizador.start()
        
#Controlador para reiniciar el juego, haciendo que las variables sean de nuevo igual a 0
def reiniciar():
    global CONTADOR,INTENTOS,ACERTADOS
    CONTADOR=0
    ACERTADOS=0
    INTENTOS=0
    temporizador.start()
    
#Funcion donde se convierte el tiempo al formato A:BC.D
def convertir(tiempo):
    #Decimas de segundos
    D =str(tiempo%10)
    tiempo =tiempo/10
    #Segundos
    C =str(tiempo%6)
    tiempo=tiempo/6
    #Segundos
    B =str(tiempo%8)
    tiempo=tiempo/10
    #Minutos
    A =str(tiempo%10)
    #Debido a que use str() procedo a concatenar la cadena para que se muestre de la forma A:BC.D
    return A+":"+B+C+"."+D

#Controlador que aumenta el contador por cada 0.1 segundos
def tick():
    global CONTADOR
    CONTADOR += 1

#Controlador que dibuja en el lienzo
def dibujar(lienzo):
    lienzo.draw_text(str(ACERTADOS) + '/' + str(INTENTOS),SUPERIORDERECHA, 45, "Green")
    lienzo.draw_text(convertir(CONTADOR),CENTRO, 60, "Yellow")

#Creando el marco
marco = simplegui.create_frame("CRONOMETRO",ANCHO,ALTO)
#Agregamos los botones y dibujar en el lienzo
marco.add_button("Empezar",empezar,100)
marco.add_button("Detener",detener,100)
marco.add_button("Reiniciar",reiniciar,100)
marco.set_draw_handler(dibujar)
#Empezamos Todo
marco.start()
#Creamos el temporizador
temporizador = simplegui.create_timer(100, tick)
#No se inicia el temporizador timer.start() porque no
#tiene que iniciar cuando se corre el programa
