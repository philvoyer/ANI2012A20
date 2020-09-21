// ANI2012A20_Color5_HSB2.pde
// Programme qui génère une image HSB avec trois variations de dégradé (touches 1, 2, 3).

// paramètres
int resolution = 512;

int rangeHue        = 360;
int rangeSaturation = 100;
int rangeBrightness = 100;

// variables
boolean regenerate;

int indexX;
int indexY;
int indexB;

int pattern;

void setup()
{
  size(512, 512);

  regenerate = true;

  pattern = int(random(1.0f, 4.0f));

  colorMode(HSB, rangeHue, rangeSaturation, rangeBrightness);
}

void draw()
{
  if (regenerate)
  {
    regenerate = false;
    generateGradient();
  }
}

void generateGradient()
{
  for (indexX = 0; indexX < resolution; ++indexX)
  {
    for (indexY = 0; indexY < resolution; ++indexY)
    {
      // sélectionner la couleur selon les indices des boucles et le pattern
      switch (pattern)
      {
        case 1: // génération d'un arc-en-ciel en mode de couleur HSB avec dégradé de la teinte (hue)
          stroke(
            map(indexX, 0, resolution, 0, rangeHue), // Hue (teinte)
            rangeSaturation,                         // Saturation
            rangeBrightness);                        // Brightness (luminosité)

          break;

        case 2: // génération d'un arc-en-ciel en mode de couleur HSB avec dégradé de la teinte (hue) et de la saturation
          stroke(
            map(indexX, 0, resolution, 0, rangeHue),         // Hue (teinte)
            map(indexY, 0, resolution, 0, rangeSaturation),  // Saturation
            rangeBrightness);                                // Brightness (luminosité)

          break;

        case 3: // génération d'un arc-en-ciel en mode de couleur HSB avec dégradé de la teinte (hue) et de la saturation et deux variations de luminosité (brightness)
          if (indexX < resolution / 2)
            indexB = resolution;
          else
            indexB = resolution / 2;

          stroke(
            map(indexX, 0, resolution, 0, rangeHue),         // Hue (teinte)
            map(indexY, 0, resolution, 0, rangeSaturation),  // Saturation
            map(indexB, 0, resolution, 0, rangeBrightness)); // Brightness (luminosité)

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
    println("ex1: gradient of hue");
  }

  if (key == '2')
  {
    pattern = 2;
    regenerate = true;
    println("ex2: gradient of hue and saturation");
  }

  if (key == '3')
  {
    pattern = 3;
    regenerate = true;
    println("ex3: gradient of hue, saturation and 2 levels of brightness");
  }
}
