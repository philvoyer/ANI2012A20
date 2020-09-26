# ANI2012A20

## Module 4 : Image

### Exemple 4.1

Un programme peut importer des images en provenance de fichiers externes, à condition qu'elles se trouvent dans un répertoire accessible par le programme. Une fois chargées en mémoire, les images peuvent ensuite être affichées et modifiées par le programme.

Un programme peut aussi importer des images de format vectoriel, par exemple les images de format .svg. Contrairement aux fichiers images standards, les fichiers images vectoriels contiennent non pas des pixels, mais une description textuelle des propriétés de la séquence de primitives vectorielles qui composent l'image.

Chaque élément du fichier correspond à une primitive et contient seulement le minimum de données liées aux propriétés permettant de la reconstruire. À partir de ces données, le programme peut rendre l'image vectorielle avec des fonctions de dessin de primitives vectorielles.

Finalement, un programme peut aussi exporter le contenu de la fenêtre d'affichage dans un fichier image. Dans le cas d'une animation, un numéro séquentiel correspondant au frame courant peut aussi être ajouté au nom de fichier.

#### Exemple 4.1.1

Importation d'un fichier image et affichage de trois instances de tailles différentes.
Le fichier à importer doit se trouver dans le répertoire */data* qui accompagne le script principal.

#### Exemple 4.1.2

Importation d'un fichier image de type vectoriel et affichage en pleine fenêtre.
Le fichier à importer doit avoir le format *.svg* et se trouver dans le répertoire */data*.

#### Exemple 4.1.3

Exportation du contenu de la fenêtre d'affichage dans différents types de format de fichier image (*.tiff*, *.jpg*, *.png*) et exportation de plusieurs frames consécutifs dans une séquence de fichiers numérotés.
Les images sont exportées dans le répertoire du script principal du programme.

### Exemple 4.2

Afin qu'un programme puisse manipuler des couleurs, elles doivent d'abord être encodées sous forme numérique. Différents formats d'encodage existent pour combler les différents besoins en termes de précision, de poids en mémoire et structure des sous-composantes de couleur.

Généralement, la couleur est encodée sur 8 bits par composante, soit 24 bits pour une couleur *RGB* (rouge, vert, bleu) et 32 bits pour une couleur *RGBA* (avec en plus une composante de transparence). Une couleur 32 bits peut être encodée directement dans une variable numérique entière (*integer*) où chaque tranche de 8 bits correspond à une des 4 composantes.

Un autre mode de couleur fréquemment utilisé est le format *HSB*, où les composantes sont la teinte (hue) la saturation et la luminosité (/brightness/).

#### Exemple 4.2.1

Programme qui génère une image en tons de gris avec un dégradé entre le blanc et le noir.

#### Exemple 4.2.2

Programme qui génère une image *RGB* avec un dégradé de la composante rouge et verte.

#### Exemple 4.2.3

Programme qui génère une image *RGB* avec trois variations de dégradé (touches 1, 2, 3).

#### Exemple 4.2.4

Programme qui génère une animation en boucle d'un arc-en-ciel avec décalage de droite à gauche.

#### Exemple 4.2.5

Programme qui génère une image *HSB* avec trois variations de dégradé (touches 1, 2, 3).

#### Exemple 4.2.6

Programme qui génère une image *RGB* avec trois variations de couleurs aléatoires (touches 1, 2, 3).

#### Exemple 4.2.7

Programme qui permet de dessiner un arc-en-ciel.

L'arc-en-ciel est généré dans une image en mémoire pendant l'initialisation du programme.

Cette technique permet d'optimiser les performances en évitant de recalculer la valeur de chaque pixel à tous les frames.

### Exemple 4.3

Le masquage est une technique qui permet de combiner deux images pour en générer une troisième. La première est une image source, la seconde est un masque et la troisième est le résultat de l'opération de masquage entre l'image source et le masque.

Le masque est une image où toutes les couleurs sont des variances de tons de gris entre le blanc et le noir. Le principe est que lorsque le masque est appliqué sur l'image source, les pixels blancs laissent passer les pixels de l'image source à 100%, les pixels noirs ne laissent pas passer les pixels de l'image source, et toutes les autres nuances de gris du masque laissent passer un pourcentage progressif de l'image source selon leur valeur entre le blanc et le noir.

#### Exemple 4.3.1

Exemple d'application d'un masque (échiquier) sur une image (dégradé).

#### Exemple 4.3.2

Exemple de l'application de différents masques sur une image (touches 1, 2, 3, 4).

### Exemple 4.4

Par un principe comparable à la technique du masquage, différents modes de composition permettent de contrôler les couleurs résultantes lorsque deux images avec transparence sont en superposition.

Par exemple, il existe le mode additif, soustractif, multiplicatif et plusieurs autres variantes qui font un mélange selon différentes proportions de la couleur des pixels en superposition.

Le principe est qu'une équation différente pour chaque mode permet de déterminer la relation entre les composantes de couleur et les composantes de transparence de chaque pixel de l'image source et de l'image en superposition.

#### Exemple 4.4.2

Démonstration du comportement de différents modes de composition sur des couleurs.
Barre d'espacement pour passer d'un ensemble de couleurs à l'autre.
Touches du clavier de 1 à 0 pour changer de mode.

#### Exemple 4.4.3

Animation de la composition entre deux images selon différents modes.
Touches du clavier de 1 à 0 pour changer de mode.

### Exemple 4.5

Une fois chargé en mémoire, un programme a accès à toutes les données sur les valeurs de couleur des pixels d'une image. Un programme donc peut manipuler ces données afin de réaliser des effets visuels par traitement d'image. Un exemple de traitement d'image pourrait être une teinte appliquée uniformément sur tous les pixels de l'image.

#### Exemple 4.5.1

Exemple où une teinte est appliquée sur une image.

#### Exemple 4.5.2

Exemple où quatre différentes teintes sont appliquées sur une même image.

#### Exemple 4.5.3

Animation de la composante alpha d'une teinte appliquée sur une image par oscillation.

### Exemple 4.6

Un autre exemple de traitement d'image est le filtrage.

Le principe du filtrage est d'appliquer un algorithme qui détermine la couleur d'un pixel en fonction de la couleur des pixels adjacents.

Cette technique est basée sur le principe du filtrage par convolution, dont les multiples variantes peuvent permettre de créer des filtres comme l'effet de flou, ainsi que plusieurs autres filtres tels que ceux offerts par les logiciels de traitement d'image.

#### Exemple 4.6.1

Exemple où un filtre différent est appliqué en alternance selon le signe d'une variable numérique animée par oscillation.

#### Exemple 4.6.2

Exemple où un filtre de flou est appliqué sur une image avec un niveau animé par oscillation.

#### Exemple 4.6.3

Exemple où différents filtres animés par oscillation sont appliqués sur une image (touches 1-6).

### Exemple 4.7

Un programme peut utiliser la vidéo comme source pour importer des images.

Que ce soit à partir d'un fichier vidéo ou d'une caméra, le principe est sensiblement le même, c'est-à-dire que chacun des frames du flux vidéo est extrait sous forme d'une image qui peut être dessinée dans une fenêtre d'affichage.

Les programmes qui utilisent la vidéo ont une dépendance vers une librairie.

Pour l'installer, dans l'éditeur de Processing, il faut aller dans le menu *Tools* > *Add Tool...* > puis dans l'onglet *Libraries* et installer la librairie *Video | GStreamer-based video library for Processing*.

#### Exemple 4.7.1

Exemple de l'importation et de la lecture d'un fichier vidéo.

La vidéo est une capture d'écran de l'exemple 3.10 en cours d'exécution.

Une teinte verte est appliquée sur la vidéo.

#### Exemple 4.7.2

Exemple de capture vidéo avec une caméra.

#### Exemple 4.7.3

Exemple de capture vidéo avec une caméra et application d'une teinte de couleur.

#### Exemple 4.7.4

Exemple de capture vidéo avec une caméra et application de différents filtres (touches 1-6).

### Exemple 4.8

Un programme peut utiliser une image comme source de donnée pour générer d'autres images.

Dans cet exemple, le programme fait la création de trois images de destination différentes à partir de l'échantillonnage d'une image source et les dessine dans la fenêtre d'affichage sous forme d'un triptyque avec un espacement horizontal et vertical.

### Exemple 4.9

Exemple classique de la balle au rebond, en version animée par programmation.

Le programme charge en mémoire une animation encodée sous forme d'une séquence d'images puis affiche successivement chacune des images en fonction de la cadence de mise à jour de l'affichage.

#### Exemple 4.9.1

Animation en boucle d'une séquence d'images.

#### Exemple 4.9.2

Animation en boucle d'une séquence d'images à l'endroit puis à l'envers à la moitié de la vitesse.

### Exemple 4.10

Exemple d'une animation de type diaporama où des images descendent perpétuellement de haut en bas à différents niveaux de profondeur.

Deux classes sont utilisées, soit une classe `Sprite` et une spécialisation de cette dernière appelée `Slide`. Les images de l'animation sont des instances de type `Slide`, une classe qui hérite de la classe `Sprite`, qui elle est plus générique et non-animée, mais qui a des propriétés et des méthodes utilisées par son descendant.

L'effet de profondeur est une illusion créée en modifiant l'opacité et la vélocité des images en fonction d'une position en Z. Les images sont triées en fonction de leur profondeur en Z pour que l'ordre de rendu soit visuellement correct.
