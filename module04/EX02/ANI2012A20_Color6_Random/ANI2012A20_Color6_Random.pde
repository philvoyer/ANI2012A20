// ANI2012A20_Color6_Random.pde
// Programme qui génère une image RGB avec trois variations de couleurs aléatoires (touches 1, 2, 3).

// paramètre
int resolution = 512;

// variables
boolean regenerate;

int indexX;
int indexY;

int pattern;

void setup()
{
  size(512, 512);

  strokeWeight(3);

  regenerate = true;

  pattern = int(random(1.0f, 4.0f));

  colorMode(RGB);
}

void draw()
{
  if (regenerate)
  {
    regenerate = false;
    generateRandomColor();
  }
}

void generateRandomColor()
{
  for (indexX = 0; indexX < resolution; indexX += 3)
  {
    for (indexY = 0; indexY < resolution; indexY += 3)
    {
      // sélectionner la couleur selon les indices des boucles et le pattern
      switch (pattern)
      {
        case 1: // couleur aléatoire en tons de gris
          int grayscale = int(random(0.0f, 256.0f));

          // configurer la couleur
          stroke(grayscale, grayscale, grayscale);
          break;

        case 2: // couleur aléatoire RGB
          stroke(
            int(random(0.0f, 256.0f)),
            int(random(0.0f, 256.0f)),
            int(random(0.0f, 256.0f)));
          break;

        case 3: // couleur aléatoire en tons de gris avec fonction de bruit
          stroke(
            int(noise(indexX, indexY) * 256.0f),
            int(noise(indexX, indexY) * 256.0f),
            int(noise(indexX, indexY) * 256.0f));
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
    println("ex1: random color with grayscale");
  }

  if (key == '2')
  {
    pattern = 2;
    regenerate = true;
    println("ex2: random color with RGB");
  }

  if (key == '3')
  {
    pattern = 3;
    regenerate = true;
    noiseSeed(millis());
    println("ex3: random color with noise");
  }
}
