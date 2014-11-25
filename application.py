#!-*- coding: utf-8-*-
"""Este Juego Adivina un numero aleatorio"""
import random
INTENTOS = 0
ERROR = 0
ALEATORIO = random.randint(1, 51)
NOMBRE = raw_input("Ingrese su nombre")
print " "
print "¡Hola!" + NOMBRE +"Bienvenido al Juego Adivina el Número"
print "INSTRUCCIONES:"
print ""
print """En Este Juego debes adivinar un número del 1 al 50,
tendrás únicamente 8 intentos para encontrar el número"""
print " "

while INTENTOS < 8:
    INTENTOS = INTENTOS + 1
    print "Elige un número"
    NUMERO = raw_input()
    try:
        NUMERO = int(NUMERO)
        ERROR = 1
    except ValueError:
        print "solo puedes ingresar números."
        print " "
        ERROR = 0
        INTENTOS = INTENTOS +1
    if NUMERO > 50 or NUMERO < 1:
        print  "intentalo de nuevo"
        print " "
    if ERROR == 1:
        if NUMERO < ALEATORIO: 
            print "Tu número es mas bajon\nintentalo de nuevo\n"
            print ""
        if NUMERO > ALEATORIO:
            print "Tu número es mas alto\nintentalo de nuevo\n"
            print " "
        if NUMERO == ALEATORIO:
            break

if NUMERO == ALEATORIO:
    print "Correcto. Usted gana."
if NUMERO != ALEATORIO:
    print "incorrecto\n Juego Terminado."
 