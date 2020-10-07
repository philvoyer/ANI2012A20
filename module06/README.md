# ANI2012A20

## Module 6 : Génératif

### Exemple 6.1

Un programme peut générer du contenu audio tel que des sons et de la musique.

#### Exemple 6.1.1

Exemple où un son est chargé en mémoire à partir d'un fichier externe (.mp3).
Le son peut ensuite être joué à partir d'une touche du clavier.

#### Exemple 6.1.2

Exemple d'un programme qui analyse le signal audio capté à partir du microphone l'ordinateur à partir de l'algorithme de transformation de Fourier (Fast Fourrier Transform) et de dessiner une représentation visuelle de l'intensité de chacune des bandes de fréquences.

#### Exemple 6.1.3

Exemple d'un programme qui simule un synthétiseur qui peut de générer des notes de musiques.
Le synthétiseur peut jouer les notes d'une gamme en DO majeur avec les touches de 1 à 8 du clavier.
Le volume et la position panoramique des notes jouées par le synthétiseur peuvent être ajustés avec les flèches du clavier.

### Exemple 6.2

Un programme peut générer dynamiquement du contenu à partir d'une fonction récursive, où chaque appel de la fonction est fait avec des valeurs différentes passées en paramètre.

Cependant, il est essentiel d'avoir une condition d'arrêt qui permet d'éviter de tomber dans une boucle infinie.

Dans cet exemple, un système fractal de Cantor est rendu par sous-division d'une ligne au tiers et au deux tiers jusqu'à un seuil de longueur minimal.

### Exemple 6.3

Un programme peut générer des formes fractales à partir d'un système de Sierpinski.

Le principe de base des systèmes de Sierpinski est de diviser récursivement des primitives géométriques telles des rectangles et des triangles.

#### Exemple 6.3.1

Un programme peut générer un système fractal de type tapis de Sierpinski avec une fonction récursive qui sous-divise le plan au tiers en huit portions égales et dont la condition d'arrêt est un seuil minimal en nombre de pixels.

#### Exemple 6.3.2

Un programme peut générer un système fractal de type triangle de Sierpinski avec une fonction récursive qui sous-divise un triangle en trois sous-triangles égaux et dont la condition d'arrêt est un nombre fixe d'itérations.

### Exemple 6.4

Un programme peut générer un système fractal de type flocon de Koch avec une fonction récursive qui sous-divise une ligne en quatre segments dont les deux du centre se joignent à un angle de 60 degrés et dont la condition d'arrêt est un nombre fixe d'itérations.

### Exemple 6.5

Un programme peut générer un système fractal de type Mandelbrot avec une relation de récurrence avec des nombres complexes qui permet de déterminer la couleur des pixels à une certaine échelle selon leur localisation dans l’espace.

Si l’équation diverge vers l’infinie (dans cet exemple, une constante prédéfinie), on utilise la couleur de l’arrière-plan. Sinon la couleur est en fonction de la valeur retournée par l’équation à un certain niveau de profondeur.

### Exemple 6.6

Un programme peut générer un système chaotique de type attracteur de Henon par l'application à chaque itération d’une équation sur deux valeurs numériques, interprétées comme une position.

### Exemple 6.7

Un programme peut générer des séquences d'éléments chainés ensemble par une relation hiérarchique à partir d'une fonction récursive. Dans cet exemple, un tentacule est animé selon ce principe.

### Exemple 6.8

Un programme peut générer des arborescences d'éléments structurées par des relations hiérarchiques à partir d'une fonction récursive. Dans cet exemple, un arbre est généré selon ce principe, avec des embranchements de proportion fixe ou aléatoire.

### Exemple 6.9

Un programme peut simuler un système de Lindenmayer (L-système) qui peut générer des structures hiérarchiques à partir d'un ensemble de symboles, d'un ensemble de règles de production et d'un axiome de départ. Dans cet exemple, trois L-systèmes classiques sont démontrés, soit une algue, un arbre et le système fractal du dragon.

### Exemple 6.10

Un programme peut générer des comportements d'animation émergents en combinant le résultat de différents comportements de mouvement déterminés individuellement au niveau de chacune des composantes d'un système dynamique. Dans cet exemple, le programme génère une animation par simulation d'un système dynamique où chaque boid à un comportement de cohésion, d'alignement et de séparation qui sont déterminés en fonction des autres boids à sa proximité.
