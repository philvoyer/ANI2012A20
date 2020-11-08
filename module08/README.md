# ANI2012A20

## Module 8 : Timing

### Exemple 8.1

Il est possible d'utiliser des scripts pour configurer un logiciel par programmation. Par exemple, *Maya* peut être configuré par des fichiers de scripts qui sont exécutés à différents stades de la procédure d'initialisation du logiciel.

D'abord, il y a le fichier 'Maya.env', qui permet de définir des variables d'environnements comme le PYTHONPATH. Ensuite il y a le fichier 'sitecustomize.py' qui est exécuté entre l'initialisation de l'interpréteur de code *Python* et le démarrage de *Maya*, puis finalement le fichier 'userSetup.py', qui est exécuté au démarrage de *Maya*.

Une fois que le logiciel *Maya* est démarré, la programmation par script permet aussi d'aller extraire des informations sur les états courants du système hôte, comme les références vers les chemins d'accès, le contenu des variables d'environnement ainsi que les symboles de portée globale (modules, fonctions, variables, etc.).

#### Exemple 8.1.1

Documentation sur les fonctions et commandes *Python* utilisées dans les exemples du cours.

#### Exemple 8.1.2

Exemples de scripts qui permettent d'extraire de l'information sur le système hôte.

#### Exemple 8.1.3

Exemple d'un script de configuration des variables d'environnement lancé au démarrage de *Maya*.

#### Exemple 8.1.4

Exemple d'un script de configuration lancé à l'initialisation de l'interpréteur *Python*, avant le démarrage de *Maya*.

#### Exemple 8.1.5

Exemple d'un script de configuration lancé au démarrage de *Maya*.

### Exemple 8.2

Ce script *Python* pour *Maya* présente des exemples de manipulations de différents types de collection comme le tuple, la liste et le dictionnaire.

### Exemple 8.3

Ce script *Python* pour *Maya* présente des exemples en lien avec l'énumération et la sélection d'éléments présents dans une scène.

### Exemple 8.4

Ce script *Python* pour *Maya* présente des manipulations d'attributs d'animation assignés à des noeuds dans une scène.

### Exemple 8.5

En animation, la pratique courante est de créer manuellement des poses clés sur une ligne de temps à partir de l'interface d'un logiciel comme *Maya*.

Il est aussi possible de créer et modifier des poses clés par programmation à partir d'un langage de script comme *Python*.

Entre autres, la plupart des éléments présents dans une scène peuvent être animés par des poses clés sur leurs attributs de transformation géométrique (translation, rotation et proportion).

La valeur courante des posés clés d'un élément sélectionné peut être visualisée dans *Maya* avec un outil qui s'appelle le *Graph Editor* (menu *Windows > Animation Editors > Graph Editor*).

#### Exemple 8.5.1

Générer une séquence d'animation par transformation de l'attribut de translation.

#### Exemple 8.5.2

Générer une séquence d'animation par transformation de l'attribut de rotation.

#### Exemple 8.5.3

Générer une séquence d'animation par transformation de l'attribut de proportion.

### Exemple 8.6

Un des avantages de l'utilisation de script *Python* avec *Maya* est de pouvoir utiliser des algorithmes pour générer ou modifier des séquences de poses clés.

Le premier et le second exemple présentent des programmes qui utilisent des fonctions mathématiques pour contrôler l'interpolation de la valeur numérique d'attributs de transformation sur une ligne de temps.

Le troisième montre comment pourrait être générée une séquence de lignes de temps contenant chacune un ensemble de poses clés.

#### Exemple 8.6.1

Création d'une séquence d'animation par oscillation de différents attributs.

La fonction trigonométrique sinus est utilisée pour générer une valeur numérique qui oscille de manière périodique en fonction d'une fréquence et d'une amplitude.

#### Exemple 8.6.2

Exemples d'interpolations de valeurs numériques avec les fonctions `lerp` et `smoothstep`.

La fonction `lerp` est une interpolation linéaire entre deux valeurs numériques en fonction d'un paramètre de temps normalisé dans l'intervalle entre zéro et un.

La fonction `smoothstep` est une interpolation avec accélération et décélération entre deux valeurs numériques en fonction d'un paramètre de temps normalisé dans l'intervalle entre zéro et un.

Les fonctions de cet exemple opèrent sur des variables numériques scalaires, mais il est aussi possible d'appliquer les mêmes algorithmes pour faire des interpolations avec des vecteurs de deux ou trois dimensions, ce qui est fort utile pour la transformation dans un espace 2D ou 3D.

#### Exemple 8.6.3

Exemple de programme qui fait la création d'une animation constituée de deux lignes de temps qui contiennent des séquences de poses clés avec des valeurs aléatoires.

L'idée est de construire une abstraction du concept de ligne de temps et d'utiliser des instances de classes et des collections pour organiser les poses clés.

Les données d'animation sont d'abord assemblées dans des instances de classes (`Animation`, `Timeline` et `Keyframe`).

Ensuite, les posés clés de notre système de lignes de temps sont injectées dans le système d'animation de *Maya* par la fonction `bake`.

### Exemple 8.7

Ce script *Python* pour *Maya* présente des exemples de fonction pour manipuler le système d'animation de *Maya* par programmation.

Par exemple, activer ou arrêter l'animation, contrôler la position de la tête de lecture de l'animation, positionner les marqueurs de début et de fin l'animation, etc.

### Exemple 8.8

Exemple de projet *Unity*.

Démonstration d'une animation construite à partir de l'éditeur de ligne de temps de *Unity*.

L'exemple vise à démontrer comment l'éditeur de ligne de temps permet de structurer une animation en plusieurs couches, avec des activations, des désactivations et des séquences de poses clés sur différents éléments de la scène.

La scène contient une sphère, un cube, un cylindre et un système de particules.

Un script *C#* permet d'atteindre directement les différentes sections de l'animation avec les touches numériques du clavier (1 à 7).

### Exemple 8.9

Exemple de projet *Unity*.

Animation d'un oiseau qui appuie sur des boutons en fonction de l'interactivité de l'utilisateur ou en mode automatique si aucune action.

L'oiseau est construit avec une structure hiérarchique composée de primitives géométriques (sphères et cylindres).

Il peut être commandé à partir du clavier (boutons Q, W, E, D, C, X, Z, A et SPACE) ou par un clic de souris directement sur un bouton.

Lorsqu'aucune action n'est faite pendant un laps de temps, l'oiseau tombe en mode automatique et son comportement est déterminé au hasard.

Les boutons sont animés directement partir de l'éditeur d'animation de *Unity* avec des poses clés sur la proportion.

### Exemple 8.10

Exemple de projet *Unity*.

Animation d'une grue avec un aimant magnétique qui permet d'interagir avec des boîtes.

La grue est construite avec une structure hiérarchique composée de primitives géométriques (sphères, cylindres et cubes).

Différentes actions au clavier permettent d'animer la grue : rotation (A, D, gauche, droit), avancer et reculer (W, S, haut, bas), monter et descendre (Q, E).

L'exemple vise à démontrer comment des interpolations de position et de rotation peuvent être utilisées pour animer de manière interactive des structures hiérarchiques.

Le champ magnétique de l'aimant est activé lorsque la touche SPACE est enfoncée.

Les boîtes sont animées par le simulateur de physique de *Unity*.
