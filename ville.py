import turtle
from turtle import *
import random

def dessiner_paysage():
    """Dessine un paysage de 3 maisons sous Turtle."""
    maison(-300,0)
    maison(-100,0)
    maison(100,0)

def maison(x, y):
    # Caractéristiques de tracé d'une maison
    largeur = 150
    hauteur_mur = 75
    hauteur_toit = 50
    nb_etages = random.randint(0,2)
    type_toit = random.randint(1,2)

    # Tracé de la maison
    i = 0
    while i <= nb_etages: # Trace le mur en fonction du nombre d'étages
        mur(x, y+i*hauteur_mur, largeur, hauteur_mur,nb_etages) # Tracé du mur
        i += 1

    toit(x, y+i*hauteur_mur, largeur, hauteur_toit,type_toit) # Tracé du toit juste au dessus du mur
    #fenetre(x,y,largeur)


def positionner(x,y):
    """
    Positionne la tortue aux coordonnées (x, y).
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rectangle(x,y,l,r):
    pendown()
    goto(x,y)
    penup()
    forward(l)
    left(90)
    forward(r)
    left(90)
    forward(l)
    goto(x,y)
    
def mur(x, y, largeur, hauteur,nb_etages):
    """
    Dessine le mur d'une maison.

    x       -- position x du coin inférieur gauche du mur
    y       -- position y du coin inférieur gauche du mur
    largeur -- largeur du mur
    hauteur -- hauteur du mur
    """
    fillcolor("yellow")
    begin_fill()
    positionner(x,y)
    goto(x,y+hauteur)
    goto(x+largeur,y+hauteur)
    goto(x+largeur,y)
    goto(x,y)
    end_fill()

"""def fenetre(x,y,nb_fenetres,largeur):
    x1 = x+largeur*1/5
    x2 = x+largeur*2/5
    x3 = x+largeur*2/5
    while i = 
    rectangle(random.choice([x1,x2,x3]),y,15,30)
"""

def toit(x, y, base, hauteur_mur,type_toit):
    """
    Dessine le toit d'une maison.

    x       -- position x du coin inférieur gauche du toit
    y       -- position y du coin inférieur gauche du toit
    base    -- largeur de la base du toit
    hauteur -- hauteur du toit
    """
    if type_toit == 1:
        positionner(x,y)
        goto(x+base/2,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)
    elif type_toit == 2:
        positionner(x,y)
        goto(x+base/3,y+hauteur_mur)
        goto(x+base*2/3,y+hauteur_mur)
        goto(x+base,y)
        goto(x,y)


print(__name__)
if __name__ == "__main__":
    # Dans le cas d'un import, cette portion de code ne sera pas exécutée 
    # car __name__ ==  "paysage" donc différent de "__main__"
    print("Exécution du code")

