#0. Importamos modulos
import simplegui
#1. Variables globales
ANCHO=700
ALTO=300
RADIO=20
CONTADOR=0
VELOCIDAD_PELOTA=[0, 0]
SUELO = ALTO-70
POSICION=[30,SUELO]
GRAVEDAD = 0.3
SALTO = False
BANDERA=False
IMAGEN=simplegui.load_image("https://i.imgur.com/F9sRwvT.jpg")
IMAGEN_TAMANIO=[ANCHO, ALTO ]
IMAGEN_CENTRO=[ANCHO//2,ALTO//2]
CAMBIO_IMAGEN=False
#2. Clases
#3. Funciones de ayuda
def iniciar(): 
    global BANDERA
    BANDERA=True
    temporizador.start()

def reiniciar():
    global CONTADOR, POSICION, VELOCIDAD_PELOTA, IMAGEN, BANDERA
    CONTADOR=0
    BANDERA=True
    POSICION=[30,SUELO]
    VELOCIDAD_PELOTA=[0, 0]
    IMAGEN=simplegui.load_image("https://i.imgur.com/HBTK9QQ.jpg")
    temporizador.start()
    
def tick():
    global CONTADOR
    CONTADOR+=1
    return CONTADOR

def calcular():
    global SALTO,IMAGEN, POSICION, VELOCIDAD_PELOTA, CAMBIO_IMAGEN
    # Update ball position
    POSICION[0] += VELOCIDAD_PELOTA[0]
    POSICION[1] += VELOCIDAD_PELOTA[1]
    if SALTO:
        VELOCIDAD_PELOTA[1] += GRAVEDAD
        if POSICION[1] >= SUELO:
            SALTO = False
            VELOCIDAD_PELOTA[1] = 0
            POSICION[1] = SUELO
    else:
        if POSICION[0]<=RADIO:
            VELOCIDAD_PELOTA[0] = -VELOCIDAD_PELOTA[0]
            if CAMBIO_IMAGEN:
                IMAGEN=simplegui.load_image("https://i.imgur.com/F9sRwvT.jpg")
            else:
                pass
        elif POSICION[0]+RADIO>=ANCHO:
            POSICION=[30,SUELO]
            VELOCIDAD_PELOTA=[0, 0]
            IMAGEN=simplegui.load_image("https://i.imgur.com/HBTK9QQ.jpg")
            CAMBIO_IMAGEN=True
        elif POSICION[1]<= RADIO or POSICION[1]+RADIO>=ALTO:
            VELOCIDAD[1]=-VELOCIDAD[1]
    
        else:
            pass

def tecla_abajo(tecla):
    global SALTO
    aceleracion=1
    if tecla==simplegui.KEY_MAP["space"] or tecla==simplegui.KEY_MAP["up"]:
        salto.play()
        SALTO = True
        VELOCIDAD_PELOTA[1] = -5
    elif tecla==simplegui.KEY_MAP["left"]:
        VELOCIDAD_PELOTA[0] -= aceleracion
    elif tecla==simplegui.KEY_MAP["right"]:
        VELOCIDAD_PELOTA[0] += aceleracion
    else:
        pass

#Funcion de entrada de una tecla
def tecla_arriba(tecla):
    pass
  
#4. Controladores
def dibujar(lienzo):
    lienzo.draw_image(IMAGEN, IMAGEN_CENTRO, IMAGEN_TAMANIO, IMAGEN_CENTRO,IMAGEN_TAMANIO)
    if BANDERA:
        calcular()
        lienzo.draw_text(str(CONTADOR), (ANCHO-60,30), 30, "Red")
        lienzo.draw_text("Happy", (320,30), 40, "Yellow")
        lienzo.draw_text("Ayuda a Happy a no chocar con nada.", (255,60), 20, "Black")
        lienzo.draw_circle(POSICION,RADIO, 10, "Yellow", "Yellow")
    else:
        lienzo.draw_text("Presiona INICIAR JUEGO para comenzar a jugar.", (190,45), 20, "Yellow")
        lienzo.draw_text("Instrucciones:" , (250,95), 18, "Red")
        lienzo.draw_text("Tecla Arriba = Saltar" , (250,125), 18, "White")
        lienzo.draw_text("Tecla espacio = Salar" , (250,155), 18, "White")
        lienzo.draw_text("Tecla derecha = Moverse a la derecha" , (250,185), 18, "White")
    
#5. Creacion del marco
marco=simplegui.create_frame("DESPENSA DE SOFY", ANCHO, ALTO)
temporizador=simplegui.create_timer(1000, tick)
salto=simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/jump.ogg")
#6. Registrar Controladores
marco.set_draw_handler(dibujar)
marco.add_button("Iniciar el Juego", iniciar)
marco.add_button("Reiniciar", reiniciar)
marco.set_keydown_handler(tecla_abajo)
marco.set_keyup_handler(tecla_arriba)
#7. Iniciar Todo
marco.start()