# ANI2012A20

## Module 2 : Structure

### Exemple 2.1

Le flot d'exécution des instructions d'un programme peut être contrôlé avec des structures logiques et des structures itératives.

#### Exemple 2.1.1

Exemples de structures logiques (**if**, **else**, **else if**, **switch**, **?:**).

#### Exemple 2.1.2

Exemples de structures itératives (**for**, **while**, **do while**).

### Exemple 2.2

Un programme peut invoquer des fonctions, qui sont soit développées par le programmeur ou qui proviennent de librairies de code déjà existant (ex. les fonctions de *Processing*).

Les fonctions permettent d'encapsuler un bloc d'instructions sous le couvert d'un identifiant et peuvent optionnellement recevoir des paramètres de différents types en entrée et retourner une valeur d'un certain type en sortie.

Une fois déclarée, une fonction peut être invoquée par son identifiant auquel on passe différentes valeurs en paramètre.

Une fonction peut aussi s'invoquer elle-même, mais seulement si elle a une condition d'arrêt qui dépend de la valeur de ses paramètres, à défaut de quoi l'exécution pourrait tomber dans une boucle infinie.

Parmi les applications des fonctions en animation, on peut citer entre autres la génération de nombres pseudo-aléatoires, le dessin vectoriel et l'interpolation d'attributs d'animation.

#### Exemple 2.2.1

Exemples de déclarations et d'invocations de fonctions simples avec entrées et sorties numériques.

#### Exemple 2.2.2

Exemples de génération de nombres pseudo-aléatoires.

Démonstration de différentes techniques pour générer des nombres aléatoires entiers ou réels.

Les nombres aléatoires permettent d'initialiser et de modifier des attributs d'animation de manière non prévisible.

#### Exemple 2.2.3

Trois exemples de fonctions récursives :

- Exemple de fonction récursive qui retourne la factorielle d'un nombre entier. La factorielle est le produit (multiplication) entre tous les nombres entiers positifs inférieurs ou égaux au nombre passé en paramètre.

- Exemple d'une fonction récursive qui retourne le nième terme de la suite de Fibonacci. Un terme de la suite de Fibonacci est la somme des deux termes précédents de la suite pour tout nombre entier plus grand que 1.

- Exemple d'une fonction récursive qui génère une boucle infinie, car elle n'a pas de condition de sortie.

#### Exemple 2.2.4

Exemple de l'animation d'un estompement progressif à partir d'une fonction.

L’estompement progressif est une animation où tout ce qui est dessiné dans la fenêtre disparait progressivement à chaque mise à jour de l’affichage pour finalement converger jusqu’à la couleur d’arrière-plan de la scène.

Cette technique est utilisée dans plusieurs de mes exemples pour créer un effet de persistance visuelle des éléments rendus dans la fenêtre d'affichage.

### Exemple 2.3

Un programme peut dessiner des points dans l'espace de la fenêtre d'affichage avec une primitive vectorielle qui a pour attributs une position sur l'axe X et Y. Le diamètre du point sera en fonction de la taille du trait.

Dans cet exemple, le programme dessine une séquence de points de taille croissante.

### Exemple 2.4

Un programme peut dessiner des lignes dans l'espace de la fenêtre d'affichage avec une primitive vectorielle qui a pour attributs les positions sur l'axe X et Y de deux sommets. La largeur de la ligne sera en fonction de la taille du trait.

Dans cet exemple, le programme dessine une séquence de lignes de taille croissante.

### Exemple 2.5

Un programme peut dessiner des triangles dans l'espace de la fenêtre d'affichage avec une primitive vectorielle qui a pour attributs les positions sur l'axe X et Y de trois sommets.

#### Exemple 2.5.1

Dans cet exemple, le programme dessine une séquence de triangles dont les trois sommets ont des positions aléatoires.

#### Exemple 2.5.2

Dans cet exemple, le programme dessine un triangle équilatérale à une position précise.

Le premier triangle est au centre de la fenêtre d'affichage.

D'autres triangles peuvent être dessinés à la position d'un clic de souris.

### Exemple 2.6

Un programme peut dessiner des rectangles ou des quadrilatères dans l'espace de la fenêtre d'affichage avec des primitives vectorielles qui ont pour attributs les positions sur l'axe X et Y de quatre sommets.

Un quadrilatère peut utiliser n'importe quelle position de l'espace de la fenêtre d'affichage pour ses quatre sommets alors qu'un rectangle est un quadrilatère dont les arêtes opposées sont alignées parallèlement sur les axes de l'espace de la fenêtre d'affichage.

Le rectangle peut donc être représenté sous forme d'une position au coin supérieur gauche ou au centre de la primitive, ainsi que d'une largeur et d'une hauteur qui permet de calculer la position de ses quatre sommets.

#### Exemple 2.6.1

Dans cet exemple, le programme dessine une séquence de rectangles de taille décroissante.

#### Exemple 2.6.2

Dans cet exemple, le programme dessine une séquence de quadrilatères dont les quatre sommets ont des positions aléatoires.

### Exemple 2.7

Un programme peut dessiner une ellipse dans l'espace de la fenêtre d'affichage avec une primitive vectorielle qui a pour attributs les positions sur l'axe X et Y du centre de la primitive, d'une largeur et d'une hauteur.

Un arc d'ellipse peut aussi être dessiné en tenant compte d'un angle de début et de fin de l'arc.

#### Exemple 2.7.1

Dans cet exemple, le programme dessine une séquence d'ellipses de taille décroissante.

#### Exemple 2.7.2

Dans cet exemple, le programme dessine une séquence d'arcs d'ellipse avec un angle croissant.

### Exemple 2.8

Un programme peut dessiner un polygone dans l'espace de la fenêtre d'affichage avec une primitive vectorielle ayant pour attributs les positions sur l'axe X et Y de chacun des ses sommets.

### Exemple 2.8.1

Dans cet exemple, le programme dessine une séquence de polygones réguliers avec un nombre de côtés croissant.

### Exemple 2.8.2

Dans cet exemple, le programme dessine des polygones en forme d'étoile.

### Exemple 2.9

Un programme peut dessiner une courbe de Bézier dans l'espace de la fenêtre d'affichage avec une primitive vectorielle qui a pour attributs les positions sur l'axe X et Y de trois points de contrôle pour une courbe de Bézier quadratique ou de quatre points de contrôle pour une courbe de Bézier cubique.

Dans cet exemple, le programme dessine une courbe de Bézier cubique avec ses quatre points de contrôle et différents repères visuels.

### Exemple 2.10

Dans cet exemple, une animation générative est créée à partir des principales notions théoriques de ce module : structures logiques, structures itératives et primitives vectorielles. 

À un intervalle régulier, des instances de primitives vectorielles sont dessinées avec des attributs aléatoires.

L'effet d'estompement progressif présenté dans l'exemple 2.2.4 est utilisé pour faire disparaitre les formes après un certain temps.

Les touches de 1 à 9 du clavier permettent d'activer ou de désactiver chaque type de primitives vectorielles et la touche 0 permet de toutes les désactiver.
