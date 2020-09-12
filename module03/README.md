# ANI2012A20

## Module 3 : Objet

### Exemple 3.1

Les chaînes de caractères sont un bon exemple d'application de la programmation orientée objet. Chaque chaîne de caractères est un objet, soit une instance de la classe String, une classe qui offre plusieurs fonctions pour construire et manipuler des données sous forme textuelle. Une chaîne de caractères est aussi une structure de données de type collection, où une séquence de caractères est stockée dans une liste ordonnée et accessible à partir d'un indice.

Dans cet exemple, démonstration de différentes techniques pour manipuler des chaînes de caractères.

### Exemple 3.2

En programmation, un tableau permet de regrouper sous une seule variable une séquence de plusieurs éléments du même type qui seront stockés dans un espace mémoire contigu. Un tableau peut avoir une ou plusieurs dimensions, mais le nombre d'éléments dans chaque dimension est fixé lors de l'instanciation. Une fois que l'espace mémoire nécessaire à chaque dimension a été alloué, les données du tableau peuvent être initialisées, lues et modifiées en y accédant avec un indice pour chaque dimension.

Dans cet exemple, animation des résultats de différents exemples de boucles et utilisation de fonctions mathématiques de base. Le résultat de chaque boucle est encodé dans un dégradé de couleur, puis il est conservé dans un tableau à deux dimensions.

### Exemple 3.3

En programmation, une structure est un regroupement de plusieurs variables de différents types sous un seul identifiant. Les structures sont utiles pour représenter des types simples qui contiennent seulement un ensemble de données sans nécessairement avoir des fonctions qui lui sont directement rattachées. Une structure peut être instanciée et chaque instance d'objet a des données indépendantes.

Dans cet exemple, instanciation et affichage de plusieurs points avec des propriétés aléatoires stockées dans une structure.

### Exemple 3.4

En programmation orientée objet, une classe est une spécification de toutes les propriétés (variables) et méthodes (fonctions) communes aux instances du type qu'elle symbolise. Le terme 'objet' est utilisé pour designer une instance d'une classe, dont les propriétés sont indépendantes des autres instances de la même classe. Lors de son instanciation, une classe est initialisée par une fonction spéciale appelée 'constructeur', qui après son exécution retournera une référence vers l'objet fraîchement alloué en mémoire, référence qui peut être assignée à une variable de type compatible.

Dans cet exemple, instanciation et affichage de plusieurs confettis avec des attributs aléatoires. Chaque confetti est une instance d'une classe avec des valeurs de propriétés différentes.

### Exemple 3.5

En programmation orientée objet, une classe peut hériter d'une autre classe. Par héritage, une classe enfant peut avoir accès à certaines propriétés et méthodes de toutes les classes qui sont un ancêtre dans la même hiérarchie de classes. Cette technique permet entre autres de manipuler à un plus haut niveau d'abstraction les données et fonctions communes à toute une descendance de types et de gérer à un plus bas niveau d'abstraction la spécialisation des types plus bas dans la hiérarchie de classes.

#### Exemple 3.5.1
Instanciation et affichage de deux formes (`Rectangle` et `Circle`) qui héritent de la même classe parent (`Shape`).

Dans ce premier exemple, chaque instance a sa propre variable et est affichée directement à partir de celle-ci.

#### Exemple 3.5.2
Instanciation et affichage de deux formes (`Rectangle` et `Circle`) qui héritent de la même classe parent (`Shape`).

Dans ce second exemple, plusieurs instances anonymes sont stockées dans un tableau sur lequel on boucle pour les afficher.

C'est grâce au principe du polymorphisme qu'il est possible de dessiner les formes sans avoir à faire un traitement particulier selon leurs types.

Puisque les classes `Rectangle` et `Circle` héritent de `Shape`, alors ils ont une fonction 'render' et il n'est pas nécessaire de faire la distinction entre les deux.

### Exemple 3.6

En programmation orientée objet, l'utilisation d'une hiérarchie de classes permet de travailler à différent niveau d'abstraction en fonction de quel niveau de spécialisation d'un type on a besoin, tout dépendamment du contexte. 

Par polymorphisme, il est possible de manipuler différentes instances d'objets de différents types avec une même interface, pourvu que chaque type partage un ancêtre commun. 

Ainsi, des fonctions peuvent être appelées avec exactement la même syntaxe pour plusieurs types d'objets différents et la fonction correspondant au bon type sera déterminée automatiquement. Le polymorphisme permet aussi d'organiser différentes instances de différents types ayant un ancêtre commun dans des structures de données de type collection. 

Par exemple, des références du type de l'ancêtre peuvent être conservées dans un tableau, si le nombre d'éléments est connu, ou dans une collection de type liste, si le nombre d'éléments peut varier en cours d'exécution.

#### Exemple 3.6.1

Animation d'une boule lumineuse avec mouvement oscillatoire.

#### Exemple 3.6.2

Animation de plusieurs boules lumineuses avec mouvement oscillatoire.

Chaque instance est gérée individuellement avec sa propre variable.

#### Exemple 3.6.3

Animation de plusieurs boules lumineuses avec mouvement oscillatoire.

Chaque instance est stockée dans un tableau à une dimension.

#### Exemple 3.6.4

Animation de plusieurs boules lumineuses avec mouvement oscillatoire.

Chaque instance est stockée dans une liste.

#### Exemple 3.6.5

Animation de plusieurs boules lumineuses avec mouvement oscillatoire.

Chaque instance est stockée dans une liste et est un descendant d'une hiérarchie de classes.

Les classes sont définies directement dans le fichier où elles sont utilisées.

#### Exemple 3.6.6

Animation de plusieurs boules lumineuses avec mouvement oscillatoire.

Chaque instance est stockée dans une liste et est un descendant d'une hiérarchie de classes.

Les classes sont définies dans des fichiers externes.

### Exemple 3.7

En programmation orientée objet, une classe peut avoir comme propriété des données primitives ainsi que des données complexes, sous forme d'instances d'autres classes. 

La relation d'association qui existe entre deux instances de classe peut prendre la forme d'une composition ou d'une agrégation. 

Avec une relation de composition, une instance d'une classe ne peut pas exister sans la présence d'une instance de l'autre classe. 

Avec une relation d'agrégation, une instance d'une classe peut exister même si l'instance de l'autre classe n'est pas confirmée au moment de la construction de l'objet.

#### Exemple 3.7.1

Exemple d'une relation de composition entre 3 composantes et 1 contenant.

#### Exemple 3.7.2

Exemple d'une relation d'agrégation entre 3 composantes et 1 contenant.

### Exemple 3.8

En programmation, le 'typecasting' est une technique qui permet de convertir une variable de type primitif ou complexe vers un autre type. 

Dans le cas des types primitifs comme les données numériques, une opération de 'cast' peut par exemple convertir un nombre entier vers un nombre réel et vice-versa.

Dans le cas des variables de types complexes, à condition que les deux types proviennent de la même hiérarchie de classes, une opération de 'cast' peut convertir une référence d'un type enfant vers un type parent ('upcasting') ou convertir une référence d'un type parent vers un type enfant ('downcasting').

Dans cet exemple, on démontre des conversions de types primitifs et complexes.

L'exemple de type complexe est une classe de type `Fruit` dont `Orange` est un descendant par héritage.

### Exemple 3.9

En guise d'exemple de programme utilisant la programmation orientée objet, voici un programme où une animation est générée par l'exécution d'un algorithme de tri appliqué sur une séquence d'objets stockés dans une collection.

Une liste d'instances est initialisée avec une valeur numérique, puis chaque itération de l'algorithme est visualisée par l'animation du déplacement de l'élément dans la séquence. 

Lorsque le tri est terminé, les objets sont mélangés au hasard et l'animation recommence.

### Exemple 3.10

En guise d'exemple de programme utilisant la programmation orientée objet, voici un exemple d'animation inspirée des automates cellulaires. 

Le principe est qu'à chaque mise à jour de l'automate, l'état de chaque cellule est mis à jour en fonction de l'état des cellules voisines. 

Les cellules sont des instances d'une classe d'un certain type et le comportement de l'animation dépend du type de cellule. 

L'exemple présente quatre différentes spécialisations de cellules avec des règles d'évolution différentes.
