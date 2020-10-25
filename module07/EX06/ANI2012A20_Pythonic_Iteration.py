# ANI2012A20_Pythonic_Iteration.py | Programmation Python avec Maya | coding=utf-8
# Exemples de structures de contrôle itératives en Python.

print "\n<début de l'exécution>"

#
# exemples d'itérations avec boucle 'for'
#

# 1. exemple de boucle 'for'

print "\n<boucle 'for' de 1 à 5 avec séquence explicite>"

for index in [1, 2, 3, 4, 5]:
  print "\tboucle %i" % (index)


# 2. exemple de boucle 'for'

print "\n<boucle 'for' de 6 à 10 avec séquence explicite>"

for index in [6, 7, 8, 9, 10]:
  print "\tboucle %i" % (index)


# 3. exemple de boucle 'for'

print "\n<boucle 'for' de 1 à 21 avec séquence explicite non continue>"

for index in [1, 2, 3, 5, 8, 13, 21]:
  print "\tboucle %i" % (index)


# 4. exemple de boucle 'for'

print "\n<boucle 'for' de -1 à 1 avec séquence explicite>"

for index in [-1, 0, 1]:
  print "\tboucle %i" % (index)


# 5. exemple de boucle 'for'

print "\n<boucle 'for' de -3 à 3 avec séquence explicite non continue>"

for index in [-3, 0, 3]:
  print "\tboucle %i" % (index)


# 6. exemple de boucle 'for'

print "\n<boucle 'for' de 0 à 9 avec intervalle qui commence à 0>"

for index in range(10):
  print "\tboucle %i" % (index)


# 7. exemple de boucle 'for'

print "\n<boucle 'for' de 1 à 9 avec intervalle qui commence à un seuil spécifique>"

for index in range(1, 10):
  print "\tboucle %i" % (index)


# 8. exemple de boucle 'for'

print "\n<boucle 'for' de 5 à 10 avec intervalle qui commence à un seuil spécifique>"

for index in range(5, 11):
  print "\tboucle %i" % (index)


# 9. exemple de boucle 'for'

print "\n<boucle 'for' de 0 à 18 avec intervalle et décalage de 3 nombres par boucle>"

for index in range(0, 20, 3):
  print "\tboucle %i" % (index)


# 10. exemple de boucle 'for'

print "\n<boucle 'for' de 0 à 8 avec intervalle et décalage de 2 nombres par boucle (pair)>"

for index in range(0, 10, 2):
  print "\tboucle %i" % (index)


# 11. exemple de boucle 'for'

print "\n<boucle 'for' de 1 à 9 avec intervalle et décalage de 2 nombres par boucle (impair)>"

for index in range(1, 10, 2):
  print "\tboucle %i" % (index)


# 12. exemple de boucle 'for'

print "\n<boucle 'for' de 10 à 1 avec intervalle décroissant>"

for index in range(10, 0, -1):
  print "\tboucle %i" % (index)


# 13. exemple de boucle 'for'

print "\n<boucle 'for' de 0 à -10 avec intervalle décroissant>"

for index in range(0, -11, -1):
  print "\tboucle %i" % (index)


# 14. exemple de boucle 'for'

print "\n<boucle 'for' de 2 à 3 avec intervalle et filtrage par séquence>"

for index in range(5)[2:4]:
  print "\tboucle %i" % (index)


# 15. exemple de boucle 'for'

print "\n<boucle 'for' de 1 à 4 avec intervalle et filtrage par séquence sur la borne inférieure>"

for index in range(5)[1:]:
  print "\tboucle %i" % (index)


# 16. exemple de boucle 'for'

print "\n<boucle 'for' de 0 à 3 avec intervalle et filtrage par séquence sur la borne supérieure>"

for index in range(5)[:4]:
  print "\tboucle %i" % (index)


# 17. exemple de boucle 'for'

print "\n<boucle 'for' sur chaque caractère d'une chaîne de caractères>"

for character in "python":
  print "\t%s" % character


# 18. exemple de boucle 'for'

print "\n<boucle 'for' sur les clés d'un dictionnaire>"

for key in {'x': 1, 'y': 2, 'z': 3}:
  print "\t%s" % key


# 19. exemple de boucle 'for'

print "\n<boucle 'for' à partir d'une fonction génératrice>"

# fonction génératrice
def iterateWithGenerator(n):
  value = 0

  while value < n:
    yield value
    value += 1

# utilisation de la fonction génératrice comme source d'itération
for index in iterateWithGenerator(10):
    print "\tboucle %i" % index


#
# exemples d'itérations avec boucle 'while'
#

# 20. exemple de boucle 'while' #3

print "\n<boucle 'while' avec aucune itération>"

while (0):
  print "\t<trace impossible>"

print "\t<aucune trace>"


# 21. exemple de boucle 'while' (en commentaire, car cause une boucle infinie)

#while (1):
#  print "\t<boucle infinie>"


# 22. exemple de boucle 'while' (en commentaire, car cause une boucle infinie)

#while (True):
#  print "\t<boucle infinie>"


# 23. exemple de boucle 'while'

print "\n<boucle 'while' de 0 à 4>"

index = 0

while (index < 5):
  print "\tboucle %i" % (index)
  index += 1


# 24. exemple de boucle 'while'

print "\n<boucle 'while' de 5 à 1>"

index = 5

while (index > 0):
  print "\tboucle %i" % (index)
  index -= 1


print "\n<fin de l'exécution>\n"
