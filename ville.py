import turtle
from turtle import *
import random

def dessiner_paysage():
    """Dessine un paysage de 3 maisons sous Turtle."""
    bgcolor("skyblue")
    soleil(200,250)
    maison(-300,0,150,75,50,random.randint(0,2),random.randint(1,2),"#817F98","#EE3510")
    maison(-100,0,150,75,50,random.randint(0,2),random.randint(1,2),"#F0D83C","#7D310A")
    maison(100,0,150,75,50,random.randint(0,2),random.randint(1,2),"#FF8E8E","#0E3918")
    nuage()

def nuage():

def soleil(x,y):
    etoile(x,y)
    positionner(x+50,y-50)
    fillcolor("yellow")
    begin_fill()
    circle(35)
    end_fill()

def etoile(x,y):
    positionner(x,y)
    fillcolor("orange")
    begin_fill()
    for i in range(5):
        forward(100)
        right(144)
    end_fill()

def maison(x, y, largeur,hauteur_mur, hauteur_toit, nb_etages, type_toit,couleur,couleur_toit):

    # Tracé de la maison
    i = 0
    while i <= nb_etages: # Trace le mur en fonction du nombre d'étages
        mur(x, y+i*hauteur_mur, largeur, hauteur_mur,couleur) # Tracé du mur
        i += 1

    toit(x, y+i*hauteur_mur, largeur, hauteur_toit,type_toit,couleur_toit) # Tracé du toit juste au dessus du mur


def positionner(x,y):
    """
    Positionne la tortue aux coordonnées (x, y).
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(x,y,l,r,couleur):
    """
    Dessine un rectangle.
    
    
    """
    fillcolor(couleur)
    begin_fill()
    positionner(x,y)
    goto(x+l,y)
    goto(x+l,+y+r)
    goto(x,y+r)
    goto(x,y)
    end_fill()
    
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

    fenetre(x,y+15,random.randint(0,4),largeur)

def fenetre(x,y,nb_fenetres,largeur):
    x1 = x+largeur*1/5
    x2 = x+largeur*2/5
    x3 = x+largeur*3/5
    x4 = x+largeur*4/5
    i = 0
    while i <= nb_fenetres:
        rectangle(random.choice([x1,x2,x3,x4]),y,15,30,"blue")
        i += 1


def toit(x, y, base, hauteur_mur,type_toit,couleur_toit):
    """
    Dessine le toit d'une maison.

    x       -- position x du coin inférieur gauche du toit
    y       -- position y du coin inférieur gauche du toit
    base    -- largeur de la base du toit
    hauteur -- hauteur du toit
    """
    if type_toit == 1:
        positionner(x,y)
        fillcolor(couleur_toit)
        begin_fill()
        goto(x+base/2,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)
        end_fill()
    elif type_toit == 2:
        positionner(x,y)
        fillcolor(couleur_toit)
        begin_fill()
        goto(x+base/3,y+hauteur_mur)
        goto(x+base*2/3,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)
        end_fill()

print(__name__)
if __name__ == "__main__":
    # Dans le cas d'un import, cette portion de code ne sera pas exécutée 
    # car __name__ ==  "paysage" donc différent de "__main__"
    print("Exécution du code")

