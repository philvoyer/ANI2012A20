// ANI2012A20_Color3_RGB2.pde
// Programme qui génère une image RGB avec trois variations de dégradé (touches 1, 2, 3).

// paramètre
int dimension = 512;

// variables
boolean regenerate;

int indexX;
int indexY;

int pattern;

void setup()
{
  size(512, 512);

  regenerate = true;

  // choisir le pattern 1, 2 ou 3 au hasard
  pattern = int(random(1.0f, 4.0f));

  // configurer le mode de couleur
  colorMode(RGB);
}

void draw()
{
  if (regenerate == true)
  {
    regenerate = false;
    generateGradient();
  }
}

void generateGradient()
{
  for (indexX = 0; indexX < dimension; ++indexX)
  {
    for (indexY = 0; indexY < dimension; ++indexY)
    {
      // sélectionner la couleur selon les indices des boucles et le pattern et
      // mapping de l'intervalle de couleur (256) sur la dimension de la fenêtre d'affichage (512)
      switch (pattern)
      {
        case 1: // génération d'un dégradé de rouge et vert
          stroke(
            map(indexX, 0, dimension, 0, 255),  // rouge
            map(indexY, 0, dimension, 0, 255),  // vert
            0);                                 // bleu
          break;

        case 2: // génération d'un dégradé de rouge et bleu
          stroke(
            map(indexX, 0, dimension, 0, 255),  // rouge
            0,                                  // vert
            map(indexY, 0, dimension, 0, 255)); // bleu
          break;

        case 3: // génération d'un dégradé de vert et bleu
          stroke(
            0,                                  // rouge
            map(indexX, 0, dimension, 0, 255),  // vert
            map(indexY, 0, dimension, 0, 255)); // bleu
          break;
      }

      // afficher un point avec cette couleur
      point(indexX, indexY);
    }
  }
}

void keyReleased()
{
  if (key == '1')
  {
    pattern = 1;
    regenerate = true;
    println("ex1: gradient of 2 color components (red & green)");
  }

  if (key == '2')
  {
    pattern = 2;
    regenerate = true;
    println("ex2: gradient of 2 color components (red & blue)");
  }

  if (key == '3')
  {
    pattern = 3;
    regenerate = true;
    println("ex3: gradient of 2 color components (green & blue)");
  }
}
