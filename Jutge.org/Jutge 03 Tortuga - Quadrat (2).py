# Què fa el programa: Feu un programa que llegeixi un número c i dibuixi un quadrat de mida c amb la cantonada inferior esquerra situada a l’orígen de la tortuga.
# Només podeu utilitzar les comandes forward, right, left, done del mòdul turtle. També podeu usar la funció read del mòdul yogi. Recordeu acabar el dibuix amb done().
# Autor: Biel Rull Simon

import turtle
c = (int(input("longitud del costat: ")))
turtle.forward(c)
turtle.left(90)
turtle.forward(c)
turtle.left(90)
turtle.forward(c)
turtle.left(90)
turtle.forward(c)
turtle.left(90)
turtle.done()