#BlackJack
#0. Importar modulos
import simplegui
import random
#1. Variables globales
# cartas−936x384−fuente :  j f i t z .com
ANCHO=600
ALTO=600
FONDO= simplegui.load_image("https://i.imgur.com/lo1gFlq.png")
FONDO_TAMANIO=[ANCHO, ALTO ]
FONDO_CENTRO=[ANCHO//2,ALTO//2]
TAMANIO_CARTA=(72,96)
CENTRO_CARTA=(36,48)
IMAGENES_CARTAS = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
#Use variables globañes utiles
CARTA_TAMANO_ATRAS=(71,96)
CENTRO_CARTAS_ATRAS=(36, 48)
IMAGENES_CARTAS_ATRAS = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")
JUGANDO=False
RESULTADO=""
GANADAS=0
PERDIDAS=0
BANDERA=False
#Defina variables globales para las cartas
#T=Trebol
#P=Picas
#C=Corazon
#D=Diamante
PALOS=("T","P","C","D")
RANGOS=("A","2","3","4","5","6","7","8","9","T","J","Q","K")
VALORES={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10}
#2. Clases
#Clase Carta
class Carta:
    def __init__(self, palo, rango):
        if (palo in PALOS) and (rango in RANGOS):
            self.palo = palo
            self.rango = rango
        else:
            self.palo = None
            self.rango = None
            print "Carta Invalida: ", palo, rango

    def __str__(self):
        return self.palo + self.rango

    def obtener_palo(self):
        return self.palo

    def obtener_rango(self):
        return self.rango

    def dibujar(self, lienzo, pos):
        carta_loc = (CENTRO_CARTA[0] + TAMANIO_CARTA[0] * RANGOS.index(self.rango), 
                    CENTRO_CARTA[1] + TAMANIO_CARTA[1] * PALOS.index(self.palo))
        lienzo.draw_image(IMAGENES_CARTAS, carta_loc, TAMANIO_CARTA, [pos[0] + CENTRO_CARTA[0], pos[1] + CENTRO_CARTA[1]], TAMANIO_CARTA)

#Definir la clase Mano      
class Mano:    
    #Cree el objeto mano
    def __init__(self):
        self.mano = []

    #regrese una cadena de caracteres que represente la mano
    def __str__(self):
        cadena = "["
        for carta in self.mano:
            cadena+= str(carta)+","            
        if cadena[-2:] ==", ":
            return cadena[0:-2]+"]"
        else:
            return cadena+"]"
    
    #Metodo que agrega una carta a la mano
    def agregar_carta(self, carta):
        self.mano.append(carta)

    #Metodo que obtiene el valor de la mano
    def obtener_valor(self):
        valor_mano = 0
        carta_az = 0
        for carta in self.mano:
            if carta.obtener_rango()=="A":
                carta_az += 1
            valor_mano += VALORES.get(carta.obtener_rango())
        if carta_az > 0 and (valor_mano + 10) <= 21:
            valor_mano += 10
        return valor_mano
    #cuente los aces como 1, se pueden y deben contar como 11
    #si el valor de la mano es menor a 21
    #calcule el valor de la mano, use reglas estandares de 21
        
    def dibujar(self, lienzo, p):
        for z in self.mano:
            carta_loc = (CENTRO_CARTA[0] + TAMANIO_CARTA[0] * RANGOS.index(z.rango), 
                    CENTRO_CARTA[1] + TAMANIO_CARTA[1] * PALOS.index(z.palo))
            lienzo.draw_image(IMAGENES_CARTAS, carta_loc, TAMANIO_CARTA, [p[0] + CENTRO_CARTA[0] + 73 * self.mano.index(z), p[1] + CENTRO_CARTA[1]], TAMANIO_CARTA)
            lienzo.draw_text("Repartidor", [50,170],20,"Black")
            lienzo.draw_text("Jugador", [50, 370],20, "Black")
        #dibuje la mano en el lienzo, pista: esto ya esta dado
        #en esta misma plantilla
        
#Defina la clase baraja
class Baraja:
    def __init__(self):
        self.baraja = []
        for palo in PALOS:
            for rango in RANGOS:
                self.baraja.append(Carta(str(palo),str(rango)))
    #cree el objeto baraja
    
    #regrese una cadena de caracteres que represente la baraja
    def __str__(self):
        cadena = "["
        for carta in self.baraja:
            cadena+= str(carta)+","            
        if cadena[-2:] ==", ":
            return cadena[0:-2]+"]"
        else:
            return cadena+"]"
    #metodo para mezclar la baraja
    def mezclar(self):
        #mezcle la baraja
        random.shuffle(self.baraja)
        #use random.shuffle

    #dele una carta al jugador de la baraja
    def dar_carta(self):
        self.carta = self.baraja[0]
        self.baraja.remove(self.carta)
        return self.carta

#3. Funcione de ayuda
#4. Controladores
#defina controladores de evento para los botones
#Controlador para el boton repartir
def repartir():
    global RESULTADO, GANADAS, PERDIDAS, JUGANDO, BANDERA, jugador, repartidor, baraja
    if JUGANDO:
        PERDIDAS+=1
        RESULTADO="Estaba Jugando. Ha perdido"
    else:
        RESULTADO="Quiere otra o se queda?"
    baraja=Baraja()
    jugador=Mano()
    repartidor=Mano()
    #carta=Carta("T","9")
    #print str(carta)
    #cada vez que se reparten se mezcla la baraja
    baraja.mezclar()
    #Se agregan 2 cartas a cada uno
    jugador.agregar_carta(baraja.dar_carta())
    jugador.agregar_carta(baraja.dar_carta())
    repartidor.agregar_carta(baraja.dar_carta())
    repartidor.agregar_carta(baraja.dar_carta())
   
    #Ya empezo el juego
    JUGANDO=True
    BANDERA=False
    #para comprobar que sumara bien los valores
    #print repartidor.obtener_valor()
    #print jugador.obtener_valor()
    #print "M A N O S"
    #print "Mano Repartidor:",str(repartidor)
    #print "Mano Jugador:",str(jugador),"\n"
    #print "Baraja:",str(baraja)
    
#Controlador para el boton dar carta   
#si la mano esta activa, dele una carta al jugador
#si se pasa, asigne un mensaje a resultado, actualice jugando y marcador  
def dar():
    global RESULTADO,PERDIDAS, JUGANDO
    #Comprueba si se está jugando
    if JUGANDO:
        jugador.agregar_carta(baraja.dar_carta())
        if jugador.obtener_valor()>21:
            RESULTADO = "Te pasaste. Has perdido."
            PERDIDAS+=1
            JUGANDO=False
        else:
            RESULTADO = "Quiere otra o se queda?"
    #Si no esta jugando no va a entregar cartas
    else:
        pass
    return PERDIDAS, RESULTADO, JUGANDO
    
#Controlador para terminar la jugada
#si la mano esta en juego dele cartas al repartidor
#hasta que el valor de su mano sea igual o mayor a 17
#asigne un mensaje a resultado, actualice jugando y marcador
def quedarse():
    global RESULTADO,PERDIDAS,GANADAS,JUGANDO,BANDERA
    JUGANDO=False
    if not BANDERA:
    #se le agregan cartas al repartidoe hasta que el valor total 
    #sumen mas de 17
        while repartidor.obtener_valor()<17:
            repartidor.agregar_carta(baraja.dar_carta())
        if repartidor.obtener_valor()>21:
            RESULTADO = "Repartidor Pierde. Vuelve a apostar?"
            GANADAS+=1
        elif repartidor.obtener_valor()>=jugador.obtener_valor():
            RESULTADO = "Repartidor Gana.Vuelve a apostar?"
            PERDIDAS+=1
        else:
            RESULTADO = "HA GANADO!!! Vuelve a apostar?"
            GANADAS+=1
        BANDERA=True
    else:
        RESULTADO="Ya no puede quedarse. Ya no esta jugando"
    return RESULTADO,PERDIDAS,GANADAS,JUGANDO,BANDERA
    
#Controlador de dibujos 
def dibujar(lienzo):
    #mire que su controlador dibuje correctamente la carta
    #con el valor de aqui abajo
    #luego borre y que dibuje las cartas en general
    lienzo.draw_image(FONDO, FONDO_CENTRO, FONDO_TAMANIO, FONDO_CENTRO,FONDO_TAMANIO)
    repartidor.dibujar(lienzo, [50, 200])    
    jugador.dibujar(lienzo, [50, 400])
    if JUGANDO:
        lienzo.draw_image(IMAGENES_CARTAS_ATRAS, CENTRO_CARTAS_ATRAS, CARTA_TAMANO_ATRAS, [50 + CENTRO_CARTAS_ATRAS[0], 200 + CENTRO_CARTAS_ATRAS[1]], TAMANIO_CARTA)
    else:
        pass
    lienzo.draw_text(RESULTADO,[250,390],20,"Blue")
    lienzo.draw_text("GANADAS: "+str(GANADAS),[480,70],15,"White")
    lienzo.draw_text("PERDIDAS: "+str(PERDIDAS),[480,90],15,"White")
    lienzo.draw_text("BlackJack",[150,50],60,"Yellow")

#5. Iniciar marco
marco = simplegui.create_frame(" B L A C K J A C K ", ANCHO, ALTO)
marco.set_canvas_background("Green")
#6. Crear botones y llamadas
marco.add_button("Reiniciar",repartir, 200)
marco.add_button("Otra",dar, 200)
marco.add_button("Me quedo",quedarse, 200)
marco.set_draw_handler(dibujar)
#7. Comenzar Todo
repartir()
marco.start()
