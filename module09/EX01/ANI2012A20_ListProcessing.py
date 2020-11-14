# ANI2012A20_ListProcessing.py | Programmation Python avec Maya | coding=utf-8
# Exemples de manipulations de listes avec fonctions lambda, map, reduce, filter et leurs équivalents avec la technique de compréhension de liste.

print "\n<début de l'exécution>\n"

# définition de quelques listes de valeurs numériques

listA = [1, 2, 3, 4, 5]
listB = [6, 7, 8, 9, 10]
listC = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


# 1. fonction lambda (x+1)

print "\n<ex1. application sur une liste d'une fonction lambda qui incrémente de 1 la valeur de chaque élément de la liste>\n"

# version 1

result = map(lambda x : x+1, listA)

print "<résultat 1.1 : %s (avec fonction map et lambda)>\n" % result

# version 2

result = [x+1 for x in listA]

print "<résultat 1.2 : %s (avec technique de compréhension de liste)>\n" % result


# 2. fonction lambda (x*2)

print "\n<ex2. application sur une liste d'une fonction lambda qui multiplie par 2 la valeur de chaque élément de la liste>\n"

# version 1

result = map(lambda x : x*2, listA)

print "<résultat 2.1 : %s (avec fonction map et lambda)>\n" % result

# version 2

result = [x*2 for x in listA]

print "<résultat 2.2 : %s (avec technique de compréhension de liste)>\n" % result


# 3. fonction lambda (x*x)

print "\n<ex3. application sur une liste d'une fonction lambda qui multiplie par elle-même la valeur de chaque élément de la liste>\n"

# version 1

result = map(lambda x : x*x, listA)

print "<résultat 3.1 : %s (avec fonction map et lambda)>\n" % result

# version 2

result = [x*x for x in listA]

print "<résultat 3.2 : %s (avec technique de compréhension de liste)>\n" % result


# 4. fonction lambda (compteurs)

print "\n<ex4. application sur une liste de listes d'une fonction lambda qui détermine le nombre d'éléments dans chaque sous-liste>\n"

# version 1

result = map(lambda x : len(x), [listA, listB, listC])

print "<résultat 4.1 : %s (avec fonction map et lambda)>\n" % result

# version 2

result = [len(x) for x in [listA, listB, listC]]

print "<résultat 4.2 : %s (avec technique de compréhension de liste)>\n" % result


# 5. fonction lambda, mapping et réduction (somme des compteurs)

print "\n<ex5. détermine la somme du nombre d'éléments dans chaque sous-liste>\n"

# version 1

result = reduce(lambda x, y: x+y, map(lambda x : len(x), [listA, listB, listC]))

print "<résultat 5.1 : %s (avec fonction map, reduce et lambda)>\n" % result

# version 2

result = "pas d'équivalent simple pour ce cas"

print "<résultat 5.2 : %s (avec technique de compréhension de liste)>\n" % result


# 6. fonction lambda et filtrage (nombres pairs)

print "\n<ex6. application d'un filtre qui retourne la sous-liste des nombres pairs d'une liste>\n"

# version 1

result = filter(lambda x: x % 2 == 0, listC)

print "<résultat 6.1 : %s (avec fonction map, filter et lambda)>\n" % result

# version 2

result = [x for x in listC if x % 2 == 0]

print "<résultat 6.2 : %s (avec technique de compréhension de liste)>\n" % result


print "\n<fin de l'exécution>\n"
