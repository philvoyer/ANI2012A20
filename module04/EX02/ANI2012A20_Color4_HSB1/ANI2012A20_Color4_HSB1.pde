// ANI2012A20_Color4_HSB1.pde
// Animation en boucle d'un arc-en-ciel avec décalage de droite à gauche.

// paramètres
int resolution = 512;
int step = 1;

// variables
int index;
int shift;
int value;

void setup()
{
  size(512, 512);
  frameRate(60);

  // configurer le mode de couleur
  colorMode(HSB, 100);

  shift = 0;
}

void draw()
{
  for (index = 0; index < resolution; ++index)
  {
    value = index + shift;
    value = cycle(value, 0, resolution);

    stroke(map(value, 0, resolution, 0, 100), 100, 100);

    line(index, 0, index, resolution);
  }

  shift += step;
  shift = cycle(shift, 0, resolution);
}

// fonction qui permet de boucler sur l'intervalle entre la borne inférieure et supérieure
int cycle(int value, int min, int max)
{
  if (value < min)
    return max - value;
  else if (value > max)
    return value - max;
  else
    return value;
}
