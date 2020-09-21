// ANI2012A20_Color1_Grayscale.pde
// Programme qui génère une image en niveaux de gris avec un dégradé entre le blanc et le noir.

// paramètre
int dimension = 256;

// variables
int indexX;
int indexY;

size(256, 256);

// configurer le mode de couleur
colorMode(RGB);

for (indexX = 0; indexX < dimension; ++indexX)
{
  for (indexY = 0; indexY < dimension; ++indexY)
  {
    // sélection de la couleur selon les indices des boucles
    stroke(indexX, indexX, indexX); // <- même valeur dans chaque composante de la couleur RGB

    // afficher un point avec cette couleur
    point(indexX, indexY);
  }
}
