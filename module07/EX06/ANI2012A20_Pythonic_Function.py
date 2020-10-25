# ANI2012A20_Pythonic_Function.py | Programmation Python avec Maya | coding=utf-8
# Exemples de définitions et d'utilisations de fonctions en Python.

import math
import maya

print "\n<début de l'exécution>\n"

# 1. une instruction simple encapsulée dans une fonction

# instruction qui n'est pas dans une fonction
print("hello world")

# la même instruction encapsulée dans une fonction
def helloworld():
  print("hello world")

helloworld()


# 2. une fonction qui retourne une chaîne de caractères

def ping():
  print "ping"
  return "pong"

print(ping())


# 3. une fonction qui affiche la valeur de deux constantes numériques réelles avec formatage à 3 décimales

def print_math_constant():
  print 'constante pi: %.3f' % math.pi
  print 'constante e: %.3f' % math.e

print_math_constant()


# 4. une fonction qui affiche la racine carrée des nombres entiers de 0 à n

def print_square_root(n):
  for index in range(n):
    print math.sqrt(index)

print_square_root(10)


# 5. une fonction avec aucun paramètre

def print_no_param():
  print "no param"


# 6. une fonction qui affiche une valeur passée en paramètre

def print_one_param(arg1):
  print "param: %r" % arg1

print_one_param("123456")


# 7. une fonction qui affiche deux valeurs passées dans deux paramètres différents

def print_two_param(arg1, arg2):
  print "param1: %r, param2: %r" % (arg1, arg2)

print_two_param("123", "456")


# 8. une fonction qui affiche deux valeurs passées en paramètre sous la forme d'une liste de paramètres sans nom (*args)

def print_two_args(*args):
  arg1, arg2 = args
  print "param0: %r, param1: %r" % (arg1, arg2)

print_two_args("321", "654")


# 9. une fonction qui affiche des valeurs passées en paramètre sous la forme d'un dictionnaire de paramètres avec nom (**kwargs)

def print_kwargs(**kwargs):
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      print "%s: %s" %(key, value)

argsAsDictionnary = {"param1": 1, "param2": 2, "param3": 3.0, "param4": "four"}

print_kwargs(**argsAsDictionnary)


# 10. une fonction récursive qui calcul le n-ième terme de la suite de Fibonacci

def fibonacci(n):
  if n is 0 or n is 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for index in range(10):
  print fibonacci(index)


# 11. exécution d'une fonction en différé

def delayed_startup():
  print "<exécution en différé de la fonction>"

# fonction qui retarde l'exécution après l'initialisation de la scène, aussitôt que du temps libre sera disponible
maya.utils.executeDeferred(delayed_startup)


print "\n<fin de l'exécution>\n"
