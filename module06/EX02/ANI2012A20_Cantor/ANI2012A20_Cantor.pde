// ANI2012A20_Cantor.pde
// Génération d'un système fractal de type Cantor.

// paramètres
float offset = 20.0f;
float minimum = 1.0f;

void setup()
{
  size(1024, 128);
  noLoop();
  strokeWeight(8);

  // invocation de la fonction récursive
  cantor(10.0f, offset, width - offset);
}

// fonction récursive qui sous-divise une ligne au tiers et au deux tiers
void cantor(float x, float y, float length)
{
  // condition d'arrêt de la fonction récursive
  if (length > minimum)
  {
    // dessiner une ligne
    line(x, y, x + length, y);

    // incrémenter la position en hauteur
    y += offset;

    // appel récursif de la sous-division de gauche
    cantor(x, y, length / 3.0f);

    // appel récursif de la sous-division de droite
    cantor(x + length * 2.0f / 3.0f, y, length / 3.0f);
  }
}
