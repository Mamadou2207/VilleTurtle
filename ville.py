from tkinter import Y
import turtle
from turtle import *
import random

def dessiner_paysage():
    """Dessine un paysage avec un nombre aléatoire maisons sous Turtle."""
    bgcolor("skyblue") # Crée un ciel bleu
    rectangle(-500,-500,1000,500,"#38b75c") # Trace une "plaine" verte
    soleil(200,250) # Trace un soleil
    for _ in range(6,12): # Trace plusieurs nuages
        taille_nuage = random.randint(10,25) # Taille du cercle du nuage sera entre 10 et 25px
        nuage(random.randint(-200,200),random.randint(150,200),taille_nuage)
    color("black") # Remet la couleur de la ligne à la normale
    for _ in range (3,8): # Trace un nombre aléatoire de maisons
        x = random.randrange(-350,350,50) # Coordonnée X des maisons sera entre -350 et 350 avec un pas de 50 
        y = 0
        largeur = 150
        hauteur_mur = 75
        hauteur_toit = 50
        nb_etages = random.randint(0,2) # Nombre d'étages aléatoires entre 0 et 2 car i sera additionné à 1 donc il y aura entre 1 et 3 étages.
        type_toit = random.randint(1,2) # Choisir aléatoirement entre deux types de toit à l'aide de deux nombres.
        maison(x, y, largeur,hauteur_mur, hauteur_toit, nb_etages, type_toit,couleur_aleatoire(),couleur_aleatoire())
    route(0,0) # Trace route

def nuage(x,y,taille_nuage):
    """
    Dessine un nuage aléatoire en taille et en forme.
    x       -- position x du premier cercle
    y       -- position y du premier cerlcle
    taille_nuage    -- taille de chaque cercle
    """
    positionner(x,y)
    fillcolor("white")
    color("white")
    for _ in range(0,10):
            penup()
            for i in range(0,20):
                if i%2==0: # Donne des chances égales d'aller soit à droite soit à gauche.
                    left(random.randint(0,360)) # Change l'angle de direction.
                else:
                    right(random.randint(0,360)) # Change l'angle de direction
            pendown()
            forward(10) # Se décaler d'une petite distance afin de retracer un cercle collé au précédent.
            begin_fill()
            circle(taille_nuage)
            end_fill()
    setheading(0) #remet la direction de la tortue à la normale

def soleil(x,y):
    """
    Trace un soleil orange et jaune dans le ciel.
    x       -- position x du début de la première pointe des rayons
    y       -- position y du début de la première pointe des rayons
    """
    etoile(x,y) # Dessiner une étoile pour représenter les "rayons" du soleil.
    positionner(x+50,y-50) # Se repositionner au centre de cette étoile.
    fillcolor("yellow")
    begin_fill()
    circle(35) # Trace le soleil avec un cercle.
    end_fill()

def etoile(x,y):
    """
    Dessine une étoile.
    x       -- position x du début de l'étoile
    y       -- position y du début de l'étoile
    """
    #Tracé de l'étoile.
    positionner(x,y)
    fillcolor("orange")
    begin_fill()
    for i in range(5):
        forward(100)
        right(144)
    end_fill()

def route(x,y):
    """
    Dessine une route avec des arbres sur les bords.
    x       -- position x du milieu de la petite base du trapèze qui se trouve en haut
    y       -- position y du milieu de la petite base du trapèze qui se trouve en haut
    """
    positionner(x,y)
    Xdebut_trapeze = xcor() # Stocker les coordonnées X actuelles en vue de les utiliser.
    Ydebut_trapeze = ycor() # Stocker les coordonnées Y actuelles en vue de les utiliser.
    fillcolor("#7c8193")
    begin_fill()
    # Tracé de la route qui est enfaite un trapèze.
    forward(100)
    goto(x+200,y-400)
    goto(x-200,y-400)
    goto(x-100,y)
    goto(x,y)
    end_fill()
    for _ in range (27): # Trace 27 arbres tout au long du bord droit de la route.
        arbre(x+100,y)
        x += 2.3 # Réduit la coordonnée X au fur et à mesure pour que les arbres soit tracées le long du bord de la route.
        y -= 10 # Réduit la cordonnée Y au fur et à mesure pour que les arbres aient une bonne visibilité.

    positionner(Xdebut_trapeze-100,Ydebut_trapeze)
    for _ in range(27): # Trace 27 arbres tout au long du bord gauche de la route.
        arbre(Xdebut_trapeze-100,Ydebut_trapeze)
        Xdebut_trapeze -= 2.8 # Réduit la coordonnée X au fur et à mesure pour que les arbres soit tracées le long du bord de la route.
        Ydebut_trapeze -= 10 # Réduit la cordonnée Y au fur et à mesure pour que les arbres aient une bonne visibilité.

def maison(x, y, largeur,hauteur_mur, hauteur_toit, nb_etages, type_toit,couleur,couleur_toit):
    """
    Dessine une maison.
    x       -- position x du coin inférieur gauche de la maison
    y       -- position y du coin inférieur gauche de la maison
    largeur -- largeur de la maison
    hauteur_mur -- hauteur de chaque mur qui compose la maison
    hauteur_toit    -- hauteur du toit
    nb_etages   -- nombre d'étages de la maison
    type_toit   -- type de toit de la maison
    couleur -- couleur des murs de la maison
    couleur_toit    -- couleur du toit de la maison
    """
    # Tracé de la maison
    i = 0
    while i <= nb_etages: # Trace le mur en fonction du nombre d'étages
        mur(x, y+i*hauteur_mur, largeur, hauteur_mur,couleur) # Tracé du mur
        i += 1
        if i == 1:
            porte(x,y,largeur)
    
    toit(x, y+i*hauteur_mur, largeur, hauteur_toit,type_toit,couleur_toit) # Tracé du toit juste au dessus du mur

def mur(x, y, largeur, hauteur,couleur):
    """
    Dessine le mur d'une maison.

    x       -- position x du coin inférieur gauche du mur
    y       -- position y du coin inférieur gauche du mur
    largeur -- largeur du mur
    hauteur -- hauteur du mur
    """
    fillcolor(couleur)
    begin_fill()
    positionner(x,y)
    goto(x,y+hauteur)
    goto(x+largeur,y+hauteur)
    goto(x+largeur,y)
    goto(x,y)
    end_fill()
    fenetre(x,y+15,random.randint(0,4),largeur) # Trace un nombre aléatoire des fois entre 1 et 4

def fenetre(x,y,nb_fenetres,largeur):
    """
    Dessine des fenêtres.
    x       -- position x du coin inférieur gauche de la fenêtre
    y       -- position y du coin inférieur gauche de la fenêtre
    nb_fenetres -- nombre de fenetres sur un étage
    largeur -- largeur de la fenêtre
    """
    # Déterminer à quelles coordonnées X la fenetre serait dessinée lorsque la largeur du mur est divisée en 7
    x1 = x+largeur*1/7
    x2 = x+largeur*2/7
    x3 = x+largeur*4/7
    x4 = x+largeur*5/7
    i = 0
    while i <= nb_fenetres: # Trace une fenêtre le nombre de fois établi.
        rectangle(random.choice([x1,x2,x3,x4]),y,15,30,"blue") # la fenêtre peut être tracée à 1,2,4 ou 5 septièmes de la largeur du mur.
        i += 1

def porte(x,y,largeur):
    """
    Dessine une porte.
    x       -- position x du coin inférieur gauche de la porte
    y       -- position y du coin inférieur gauche de la porte
    largeur -- largeur de la porte
    """
    rectangle(x+largeur*3/7,y,15,30,"#5b270f") # Trace un rectangle à la façon d'une porte

def toit(x, y, base, hauteur_mur,type_toit,couleur_toit):
    """
    Dessine le toit d'une maison.

    x       -- position x du coin inférieur gauche du toit
    y       -- position y du coin inférieur gauche du toit
    base    -- largeur de la base du toit
    hauteur -- hauteur du toit
    type_toit -- type du toit entre deux options
    couleur_toit -- couleur du toit
    """
    if type_toit == 1:
        #Tracé d'un toit pointu
        positionner(x,y)
        fillcolor(couleur_toit)
        begin_fill()
        goto(x+base/2,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)
        end_fill()
    elif type_toit == 2:
        # Tracé d'un toit aplati sur le sommet
        positionner(x,y)
        fillcolor(couleur_toit)
        begin_fill()
        goto(x+base/3,y+hauteur_mur)
        goto(x+base*2/3,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)
        end_fill()

def couleur_aleatoire():
    """
    Génère aléatoirement une couleur hexadécimale
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_code = f"#{r:02x}{g:02x}{b:02x}" # Assemble les valeurs RGB
    return color_code

def arbre(x,y):
    """
    Trace un arbre.
    x       -- position x du coin inférieur gauche du tronc de l'arbre
    y       -- position y du coin inférieur gauche du tronc de l'arbre
    """
    tronc(x,y) 
    feuillage(x,y,15)
    
def tronc(x,y):
    """
    Dessine un tronc.
    x       -- position x du coin inférieur gauche du tronc
    y       -- position y du coin inférieur gauche du tronc
    """
    # Tracé du tronc de l'arbre.
    rectangle(x,y,8,15,"brown")

def feuillage(x,y,taille_feuillage):
    """
    Dessine des feuilles.
    x       -- position x du début du cercle qui fera office de feuillage
    y       -- position y du début du cercle qui fera office de feuillage
    taille_feuillage    -- taille du cercle qui fera office de feuillage
    """
    # Tracé du feuillage de l'arbre.
    positionner(x+4,y+15)
    fillcolor("#076b2d")
    begin_fill()
    circle(taille_feuillage)
    end_fill()

def positionner(x,y):
    """
    Positionne la tortue aux coordonnées (x, y).
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(x,y,l,r,couleur):
    """
    Dessine un rectangle avec des dimensions et position variables.
    x       -- position x du coin inférieur gauche du rectangle
    y       -- position y du coin inférieur gauche du rectangle
    l -- largeur du rectangle
    r -- hauteur du rectangle
    """
    # Tracé du rectangle.
    fillcolor(couleur)
    begin_fill()
    positionner(x,y)
    goto(x+l,y)
    goto(x+l,+y+r)
    goto(x,y+r)
    goto(x,y)
    end_fill() 

print(__name__)
if __name__ == "__main__":
    # Dans le cas d'un import, cette portion de code ne sera pas exécutée 
    # car __name__ ==  "paysage" donc différent de "__main__"
    print("Exécution du code")
