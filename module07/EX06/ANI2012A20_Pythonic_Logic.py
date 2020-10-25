# ANI2012A20_Pythonic_Logic.py | Programmation Python avec Maya | coding=utf-8
# Exemples de structures de contrôle logiques en Python.

print "\n<début de l'exécution>\n"

#
# paramètres du programme
#

# valeur booléenne à comparer
condition = True

# valeur numérique à comparer
number = 3

# valeurs d'une borne supérieure et inférieure utilisées pour comparaison
thresholdMin = 1
thresholdMax = 10


# 1. valider si une expression booléenne est équivalente à VRAI (une expression sans opérateur est équivalente à '== True')

if condition:
  print "le résultat de la validation est VRAI"
else:
  print "le résultat de la validation est FAUX"


# 2. valider si une expression booléenne n'est pas équivalente à VRAI (l'opérateur 'not' inverse la valeur de l'expression)

if not condition:
  print "le résultat de la validation est VRAI"
else:
  print "le résultat de la validation est FAUX"


# 3. valider si une expression booléenne est équivalente à VRAI (avec l'opérateur '==')

if condition == True:
  print "le résultat de la validation est VRAI"
else:
  print "le résultat de la validation est FAUX"


# 4. valider si une expression booléenne est équivalente à FAUX (avec l'opérateur '!=')

if condition != True:
  print "le résultat de la validation est VRAI"
else:
  print "le résultat de la validation est FAUX"


# 5. valider si une expression booléenne est équivalente à FAUX (avec l'opérateur '<>' qui est équivalent à '!=')

if condition <> True:
  print "le résultat de la validation est VRAI"
else:
  print "le résultat de la validation est FAUX"


# 6. branchement conditionnel avec 'if', 'else' et opérateur de comparaison '<' (plus petit que)

if number < thresholdMin:
  print "la valeur %i est plus petite que %i ? VRAI" % (number, thresholdMin)
else:
  print "la valeur %i est plus petite que %i ? FAUX" % (number, thresholdMin)


# 7. branchement conditionnel avec 'if', 'else' et opérateur de comparaison '>' (plus grand que)

if number > thresholdMax:
  print "la valeur %i est plus grande que %i ? VRAI" % (number, thresholdMax)
else:
  print "la valeur %i est plus grande que %i ? FAUX" % (number, thresholdMax)


# 8. branchement conditionnel avec 'if', 'else' et opérateur de comparaison '<' (plus petit ou égal à)

if number <= thresholdMin:
  print "la valeur %i est plus petite ou égale à %i ? VRAI" % (number, thresholdMin)
else:
  print "la valeur %i est plus petite ou égale à %i ? FAUX" % (number, thresholdMin)


# 9. branchement conditionnel avec 'if', 'else' et opérateur de comparaison '>' (plus grand ou égal à)

if number >= thresholdMax:
  print "la valeur %i est plus grande ou égale à %i ? VRAI" % (number, thresholdMax)
else:
  print "la valeur %i est plus grande ou égale à %i ? FAUX" % (number, thresholdMax)


# 10. séquence de 2 branchements conditionnels avec 'if',  'elif', et 'else'

if number > thresholdMax:
  print "la valeur %i est plus grande que la borne supérieure %i" % (number, thresholdMax)
elif number < thresholdMin:
  print "la valeur %i est plus petite que la borne inférieure %i" % (number, thresholdMin)
else:
  print "la valeur %i est entre la borne inférieure %i et supérieure %i" % (number, thresholdMin, thresholdMax)


# 11. branchement conditionnel sous forme compacte (branchementVrai if condition else branchementFaux )

condition = False if condition == True else True

if condition:
  print "branchement 1"
else:
  print "branchement 2"


# 12. séquence de branchements conditionnels

if condition:
  print "branchement 0"
elif number == 1:
  print "branchement 1"
elif number == 2:
  print "branchement 2"
elif number == 3:
  print "branchement 3"
elif number == 4:
  print "branchement 4"
elif number == 5:
  print "branchement 5"
else:
  print "branchement paredéfaut"


# 13. branchements conditionnels multiples

number = 6

switch = {
  1: "branchement 1",
  2: "branchement 2",
  3: "branchement 3",
  4: "branchement 4",
  5: "branchement 5"}

print switch.get(number, "branchement par défaut")


print "\n<fin de l'exécution>\n"
