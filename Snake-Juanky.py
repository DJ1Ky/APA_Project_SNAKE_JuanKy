# Joc de l'Snake fet a Python, per princiants 
# Fet per: Juan C.

import turtle       # s'utilitza per a desenvolupar coneptes d'una manera meés entretinguda
import time         # l'utilitzarem per a modificar els temps d'animació del joc


posposar = 0.11  # per a retrasar 0.1 milèsimes de segon l'execució del programa

'''
fletxa = turtle.Turtle()  # creem la fletxa que apuntará la direcció de la serp

for i in range (0,4):    # creem el loop for per optimitzar el codi de les dues instruccions 
    fletxa.forward(100)  # la fletxa avançará 100 posicions 
    fletxa.left(90)      # la fletxa fará un gir de 90 graus cap a l'esquerra

'''


# CONFIGURACIÓ DE LA FINESTRA DE JOC 

finestra = turtle.Screen()                      # creem la finestra (element Screen()) on es desenvolupará el nostre joc (titol del joc, background, colors, etc.
finestra.title("SNAKE GAME")                    # li donem un títol al joc 
finestra.bgcolor("blue")                        # canviem el color de fons de la finestra 
finestra.setup(width = 693 , height = 693)      # redimensionem la finestra amb les mesures desitjades  
finestra.tracer(0)                              # fará que les animacions siguin una mica més agradables als nostres ulls i desactiva les actualitzacions de la pantalla 


# CREACIÓ DEL CAP DE LA SERP 

cap = turtle.Turtle()           # creem un objecte turtle perque es mostri algo a la pantalla 
cap.speed(0)                    # per a que s'inicii la pantalla, el cap de la serp estigui des de l'inici
cap.shape("square")             # canviem la forma del cap a quadrada
cap.color("yellow")             # li donem un color al cap de la serp
cap.penup()                     # amb aquest comand, tot i que el cap de la serp es mogui, no hi haurá rastre o estela
cap.goto(0,0)                   # començará a la posició (0,0) de la pantalla 
cap.direction = "stop"         # amb aixó direccionem el cap de la serp en la direcció que marquem amb les fletxes del teclat. 
                                # Amb l'stop, li diem que no volem que es mogui en cap direcció fins que es faci click a alguna direcció


# FUNCIONS PER A CAMBIAR LA DIRECCIÓ DEL CAP DE LA SERP 

# la funció per a que la direcció de la funció vagi cap adalt

def adalt():
    cap.direction = "up"

# la funció per a que la direcció de la funció vagi cap abaix

def abaix():
    cap.direction = "down"

# la funció per a que la direcció de la funció vagi cap a l'esquerre

def esquerre():
    cap.direction = "left"

# la funció per a que la direcció de la funció vagi cap a la dreta 

def dreta():
    cap.direction = "right"


# FUNCIONS PER EL MOVIMENT DE LA SERP 

def moviment():

    if cap.direction == "down":     # si la direcció del cap és "down" ("abaix"), en comptes de "stop", es direccionará cap abaix.
        y = cap.ycor()              # per a que s'envagi cap abaix, hem de modificar el nostre eix Y i que el cap baixi. Obtenim així la coordenda Y del cap de la serp i la guardem a la variable y.
        cap.sety(y - 15)            # aquí fem un set de la cordenada en que es mogui 20 píxels cap abaix cada cop que s'activi la funció.
    
    if cap.direction == "up":       # si la direcció del cap és "up" ("adalt"), en comptes de "stop", es direccionará cap adalt.
        y = cap.ycor()              # per a que s'envagi cap adalt, hem de modificar el nostre eix Y i que el cap pugi. Obtenim així la coordenda Y del cap de la serp i la guardem a la variable y.
        cap.sety(y + 15)            # aquí fem un set de la cordenada en que es mogui 20 píxels cap adalt cada cop que s'activi la funció.

    if cap.direction == "right":    # si la direcció del cap és "right" ("dreta"), en comptes de "stop", es direccionará cap a la dreta e n l'eix X.
        x = cap.xcor()              # per a que s'envagi cap a ladreta, hem de modificar el nostre eix X i que el cap giri. Obtenim així la coordenda X del cap de la serp i la guardem a la variable x.
        cap.setx(x + 15)            # aquí fem un set de la cordenada en que es mogui 20 píxels cap a la dreta cada cop que s'activi la funció.

    if cap.direction == "left":     # si la direcció del cap és "left" ("esquerre"), en comptes de "stop", es direccionará cap a l'esquerra en l'eix X.
        x = cap.xcor()              # per a que s'envagi cap a l'esquerre, hem de modificar el nostre eix X (absices de la pantalla) i que el cap giri. Obtenim així la coordenda X del cap de la serp i la guardem a la variable x.
        cap.setx(x - 15)            # aquí fem un set de la cordenada en que es mogui 20 píxels cap a l'esquerre cada cop que s'activi la funció.
    
    

# CONFIGURACIÓ DEL TECLAT 

finestra.listen()                       # li diem a la pantalla que estigui atenta i escoltant les ordres del teclat 
finestra.onkeypress(adalt, "Up")        # si es prem una tecla del teclat, els parámetres que li pasaré a la funció son als que el cap de la serp reaccionará. La primera lletra de la vocal del segon parámetre, ha de ser majúscula per fer referéncia a una tecla del teclat.
finestra.onkeypress(abaix, "Down")
finestra.onkeypress(esquerre, "Left")
finestra.onkeypress(dreta, "Right")     


# MENJAR PER A LA SERP

food = turtle.Turtle()       # creem un objecte turtle perque es mostri algo a la pantalla, en aquest cas, el menjar de la serp per a que creixi 
food.speed(0)                # per a que s'inicii la pantalla, el menjar estigui des de l'inici
food.shape("circle")         # canviem la forma del menjar a circular
food.color("red")            # li donem un color, en aquest cas vermell
food.penup()                 # amb aquest comand, tot i que el food de la serp es mogui, no hi haurá rastre o estela
food.goto(0,100)             # començará a la posició (0,100) de la pantalla 

     
# FUNCIÓ LOOP PRINCIPAL 

while True:                     # creem un bucle principal, ja que será uhn bucle infinit que fins que no li donem ordre de que surti del joc, mai acabará.
    finestra.update()           # actuaqlitzarem la pantalla constantment, conforme es faci "run" del bucle s'anirá actualizant 
    moviment()                  # iniciem la funció de moviment 
    time.sleep(posposar)        # per a que el programa no s'executi tan rápid 



input("Press Enter to continue...")     # la finestra s'aturará fins que es faci click al ENTER
