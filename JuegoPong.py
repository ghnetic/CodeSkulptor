#Juego "Pong" donde el usuario mueve las paletas para poder golpear la pelota 
#0. Importamos modulos
import simplegui
import random
#1. Variables globales
ANCHO=600
ALTO=400
RADIO=20
PAD_ANCHO=8
PAD_ALTO=80
MEDIO_PAD_ANCHO=PAD_ANCHO/2
MEDIO_PAD_ALTO=PAD_ALTO/2
JUGADOR_1=0
JUGADOR_2=0
IZQUIERDA=False
DERECHA=True
POSICION=[ANCHO/2,ALTO/2]
VELOCIDAD_PALETA=10
POSICION=[]
VELOCIDAD_PELOTA=[]    
POSICION_PAL_1=[MEDIO_PAD_ANCHO, ALTO/2]
VEL_PALETA_1=[0, 0]
POSICION_PAL_2=[ANCHO - MEDIO_PAD_ANCHO, ALTO/2]
VEL_PALETA_2=[0, 0]
#2. Clases
#3. Funciones de ayuda
#Funcion para crear una nueva pelota cada vez que se anote para algun lado
def nueva_pelota(direccion):
    global POSICION,VELOCIDAD_PELOTA
    POSICION=[ANCHO/2,ALTO/2] 
    if DERECHA:
        VELOCIDAD_PELOTA=[2,-2]
    elif IZQUIERDA:
        VELOCIDAD_PELOTA=[-2,2]
    else:
        pass
    VELOCIDAD_PELOTA = [-random.randrange(2, 4),-random.randrange(1, 3)]
    if direccion:
        VELOCIDAD_PELOTA[0] = -VELOCIDAD_PELOTA[0]
    else:
        pass
        
#Funcion que actualiza la pelota, y anota en el marcador
def pelota():
    global JUGADOR_1,JUGADOR_2
    if (POSICION[1] <= RADIO or POSICION[1] >= (ALTO -1) - RADIO):   
            VELOCIDAD_PELOTA[1] = -VELOCIDAD_PELOTA[1]        
    if POSICION[0] <= (PAD_ANCHO + RADIO):
        if (POSICION_PAL_1[1] - MEDIO_PAD_ALTO <= POSICION[1] <= POSICION_PAL_1[1] + MEDIO_PAD_ALTO):
            VELOCIDAD_PELOTA[0] = -(VELOCIDAD_PELOTA[0] + VELOCIDAD_PELOTA[0] * 0.1)  
        else:  
            JUGADOR_2 += 1
            nueva_pelota(DERECHA)        
    if POSICION[0] >= (ANCHO -1 - PAD_ANCHO - RADIO):        
        if (POSICION_PAL_2[1] - MEDIO_PAD_ALTO <= POSICION[1] <=
            POSICION_PAL_2[1] + MEDIO_PAD_ALTO):            
            VELOCIDAD_PELOTA[0] = -(VELOCIDAD_PELOTA[0] + VELOCIDAD_PELOTA[0] * 0.1)  
        else:
            JUGADOR_1 += 1    
            nueva_pelota(IZQUIERDA)    
    POSICION[0] += VELOCIDAD_PELOTA[0]
    POSICION[1] += VELOCIDAD_PELOTA[1]

#Funcion de entrada de una tecla          
def tecla_abajo(tecla):
    global VEL_PALETA_1,VEL_PALETA_2 
    if (tecla==simplegui.KEY_MAP["up"]):
        VEL_PALETA_1 = [0, -VELOCIDAD_PALETA]
    elif (tecla==simplegui.KEY_MAP["down"]):
        VEL_PALETA_1 = [0, VELOCIDAD_PALETA]
    if (tecla==simplegui.KEY_MAP["w"]):
        VEL_PALETA_2 = [0, -VELOCIDAD_PALETA]
    elif (tecla==simplegui.KEY_MAP["s"]):
        VEL_PALETA_2 = [0, VELOCIDAD_PALETA]
    else:
        pass

#Funcion de entrada de una tecla
def tecla_arriba(tecla):
    global VEL_PALETA_1,VEL_PALETA_2
    if (tecla==simplegui.KEY_MAP["up"] or tecla==simplegui.KEY_MAP["down"]):
        VEL_PALETA_1=[0, 0]
    elif (tecla==simplegui.KEY_MAP["w"] or tecla==simplegui.KEY_MAP["s"]):
        VEL_PALETA_2=[0, 0]
    else:
        pass
        
#4. Controladores de evento
#Controlador para un juego nuevo
def juego_nuevo():
    global JUGADOR_1,JUGADOR_2, POSICION_PAL_1,POSICION_PAL_2
    POSICION_PAL_1=[MEDIO_PAD_ANCHO, ALTO/2]
    POSICION_PAL_2=[ANCHO - MEDIO_PAD_ANCHO, ALTO/2]
    JUGADOR_1=0
    JUGADOR_2=0
    nueva_pelota(IZQUIERDA)
    
#Controlador que se encarga que las paletas no se salgan del lienzo
def actualizar_paletas():
    POSICION_PAL_1[1] += VEL_PALETA_1[1]
    POSICION_PAL_2[1] += VEL_PALETA_2[1]
    if (POSICION_PAL_1[1] <= MEDIO_PAD_ALTO or POSICION_PAL_1[1] >= ALTO - MEDIO_PAD_ALTO):
        POSICION_PAL_1[1] -= VEL_PALETA_1[1]   
    if (POSICION_PAL_2[1] <= MEDIO_PAD_ALTO or POSICION_PAL_2[1] >= ALTO - MEDIO_PAD_ALTO):   
        POSICION_PAL_2[1] -= VEL_PALETA_2[1]

#Controlador de Dibujo        
def dibujar(lienzo):
    global POSICION_PAL_1,POS_PAL_2
    actualizar_paletas()
    pelota() 
    #Dibujar cancha del pong
    lienzo.draw_line([ANCHO/2,0],[ANCHO/2,ALTO],1,"White")
    lienzo.draw_line([PAD_ANCHO,0],[PAD_ANCHO,ALTO],1,"White")
    lienzo.draw_line([ANCHO-PAD_ANCHO,0],[ANCHO-PAD_ANCHO,ALTO],1,"White")
    lienzo.draw_circle([ANCHO/2,ALTO/2],10,1,"White","Green")
    #Dibujar paletas
    lienzo.draw_line((POSICION_PAL_1[0], POSICION_PAL_1[1] - MEDIO_PAD_ALTO), (POSICION_PAL_1[0], POSICION_PAL_1[1] + MEDIO_PAD_ALTO), PAD_ANCHO + 2, "Black")
    lienzo.draw_line((POSICION_PAL_2[0], POSICION_PAL_2[1] - MEDIO_PAD_ALTO), (POSICION_PAL_2[0], POSICION_PAL_2[1] + MEDIO_PAD_ALTO), PAD_ANCHO + 2, "Black")
    #Dibujar el marcador
    lienzo.draw_text(str(JUGADOR_1), (ANCHO/2-80, 120), 65, "Red")
    lienzo.draw_text(str(JUGADOR_2), (ANCHO/2+50, 120), 65, "Blue")
    lienzo.draw_circle(POSICION,RADIO,3,"White","White")
    
#5. Creación del marco
marco=simplegui.create_frame("JUEGO PONG C:",ANCHO,ALTO)
#6. Registro de controladores de evento
marco.set_canvas_background("Green")
marco.set_draw_handler(dibujar)
marco.set_keydown_handler(tecla_abajo)
marco.set_keyup_handler(tecla_arriba)
marco.add_button("Vuelve a empezar", juego_nuevo)
#7. Iniciamos todo
juego_nuevo()
marco.start()
