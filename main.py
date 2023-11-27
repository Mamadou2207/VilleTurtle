import turtle       # Module turtle
import ville             # Nom arbitraire du module contenant les fonctions de dessin

turtle.hideturtle()      # Masque la tortue
turtle.tracer(1, 0)      # Accélère le tracé
ville.dessiner_paysage() # Génère le paysage aléatoire 
turtle.done()            # Boucle des événements
print("Exécution du code main")