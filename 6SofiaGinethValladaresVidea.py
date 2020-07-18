#Juego de cartas, donde el usuario presiona una carta y debe
#ir encontrando su pareja
#0. Importar Modulos
import simplegui
import random
#1. Variables Globales
ANCHO=800
ALTO=100
TURNO=0
MOSTRAR=[]
AUXILIAR=0
UNO=simplegui.load_image("https://i.imgur.com/hslVkVI.jpg")
DOS=simplegui.load_image("https://i.imgur.com/VtVfd6h.jpg")
TRES=simplegui.load_image("https://i.imgur.com/DeySWza.jpg")
CUATRO=simplegui.load_image("https://i.imgur.com/zwkjpkm.jpg")
CINCO=simplegui.load_image("https://i.imgur.com/74WGqZu.jpg")
SEIS=simplegui.load_image("https://i.imgur.com/uzVfTxy.jpg")
SIETE=simplegui.load_image("https://i.imgur.com/fB6BqdN.jpg")
OCHO=simplegui.load_image("https://i.imgur.com/qg7laPt.jpg")
CARTAS=[UNO,DOS,TRES,CUATRO,CINCO, SEIS, SIETE, OCHO]
VARAJA=list(CARTAS)+list(CARTAS)
IMAGEN=simplegui.load_image("https://i.imgur.com/pHMuwwv.jpg")
NINGUNA=16
IMAGEN_CENTRO=[IMAGEN.get_width()//2,IMAGEN.get_height()//2]
IMAGEN_TAMANIO=[IMAGEN.get_width(), IMAGEN.get_height()]
#2. Clases
#3. Funciones de Ayuda
#Funcion que mezcla la varaja
#Añade cartas 'alreves' o sea con valor=0
def inicio():
    global MOSTRAR,AUXILIAR,TURNO
    MOSTRAR=[]
    AUXILIAR=0
    TURNO=0
    random.shuffle(VARAJA)
    mensaje.set_text("Turnos=" + str(TURNO)) 
    for carta in range(NINGUNA):
        MOSTRAR.append(0)
    
#Funcion que se encarga de obtener la posicion al hacer click,
#Verifica si la carta ya fue seleccionada
#Incrementa los turnos
#Determina si ambas cartas son iguales
def calculo(posicion):
    global AUXILIAR,TURNO, indice_1,indice_2
    if MOSTRAR[posicion[0]//50]==0:
        if AUXILIAR==0:
            AUXILIAR=1
            indice_1 = posicion[0]//50
        elif AUXILIAR==1:
            AUXILIAR=2
            indice_2=posicion[0]//50
            TURNO+=1
        else:
            if VARAJA[indice_1]!=VARAJA[indice_2]:
                MOSTRAR[indice_1]=0
                MOSTRAR[indice_2]=0
            AUXILIAR=1 
            indice_1=posicion[0]//50
        mensaje.set_text("Turnos=" + str(TURNO))
    MOSTRAR[posicion[0]//50]=1

#4. Constructores
#Constructor que se encarga de llamar a la funcion calculos
def click(mouse):
    calculo(mouse)
                            
#Constructor de dibuja en el lienzo  
def dibujar(lienzo):
    for carta in range(len(VARAJA)):
        if MOSTRAR[carta] == 1:
            lienzo.draw_image(VARAJA[carta],(VARAJA[carta].get_width()/2, VARAJA[carta].get_height()/2),(VARAJA[carta].get_width(),VARAJA[carta].get_height()), [IMAGEN_TAMANIO[0]/2+IMAGEN_TAMANIO[0]*carta, 50],IMAGEN_TAMANIO )
            #lienzo.draw_text(str(VARAJA[carta]), [ANCHO/16*carta+20, ALTO/2+10], 24, "Blue")
        else:
            lienzo.draw_image(IMAGEN,(IMAGEN.get_width()/2, IMAGEN.get_height()/2),(IMAGEN.get_width(),IMAGEN.get_height()), [IMAGEN_TAMANIO[0]/2+IMAGEN_TAMANIO[0]*carta, 50],IMAGEN_TAMANIO)

#5. Crear marco
print 
marco = simplegui.create_frame("JUEGO DE CARTAS", 800, 100)
#6. Registrar controles de evento
marco.add_button("Reiniciar", inicio)
mensaje=marco.add_label("Turno=0")
marco.set_mouseclick_handler(click)
marco.set_draw_handler(dibujar)
marco.set_canvas_background("White")
#7. Iniciar todo
inicio()
marco.start()