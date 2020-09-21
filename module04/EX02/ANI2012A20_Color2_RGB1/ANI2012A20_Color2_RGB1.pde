// ANI2012A20_Color2_RGB1.pde
// Programme qui génère une image RGB avec un dégradé de la composante rouge et verte.

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
    stroke(indexX, indexY, 0);

    // afficher un point avec cette couleur
    point(indexX, indexY);
  }
}
