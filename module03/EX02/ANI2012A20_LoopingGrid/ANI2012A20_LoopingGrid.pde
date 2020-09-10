// ANI2012A20_LoopingGrid.pde
// Animation des résultats de différents exemples de boucles et
// utilisation de fonctions mathématiques de base.
// Le résultat de chaque boucle est encodé dans un dégradé de couleur,
// puis il est conservé dans un tableau à deux dimensions.

// paramètres
int diameter = 32;

color colorStroke = color(91, 0, 15);

// variables
int frame;

int index;

int indexX;
int indexY;

int divisionX;
int divisionY;

int positionX;
int positionY;

int offsetX;

int colorStep;

int shift;

// tableau à deux dimensions qui contient le résultat de chaque boucle
int[][] table;

void setup()
{
  size(960, 322);
  frameRate(10);
  strokeWeight(4);
  stroke(colorStroke);
  rectMode(CORNER);

  shift = 0;
  frame = 0;

  divisionX = int(width / float(diameter));
  divisionY = int(height / float(diameter));

  colorStep = int(255.0f / divisionX);

  // instanciation du tableau à deux dimensions
  table = new int[divisionX][divisionY];

  // initialisation du tableau
  for (indexX = 0; indexX < divisionX; ++indexX)
  {
    for (indexY = 0; indexY < divisionY; ++indexY)
    {
      table[indexX][indexY] = 0;
    }
  }

  // 1. boucle croissante
  for (index = 0; index < divisionX; ++index)
  {
    table[index][0] = colorStep * index;
  }

  // 2. boucle décroissante
  for (index = divisionX - 1; index >= 0; --index)
  {
    table[index][1] = colorStep * (divisionX - index);
  }

  // 3. boucle croissante avec incrémentation de 2 sur les indices pairs
  for (index = 0; index < divisionX; index += 2)
  {
    table[index][2] = colorStep * index;
  }

  // 4. boucle croissante avec incrémentation de 2 sur indices impairs
  for (index = 1; index < divisionX; index += 2)
  {
    table[index][3] = colorStep * index;
  }

  // 5. boucle croissante avec incrémentation de 3
  for (index = 0; index < divisionX; index += 3)
  {
    table[index][4] = colorStep * (index + 2);
  }

  // 6. boucle croissante avec mapping selon une fonction trigonométrique (sinus de 90 degrés par indice)
  for (index = 0; index < divisionX; ++index)
  {
    table[index][5] = int(map(sin(radians(index * 90.0f)), -1.0f, 1.0f, 0.0f, 255.0f));
  }

  // 7. boucle croissante avec mapping selon une fonction trigonométrique (cosinus de 90 degrés par indice)
  for (index = 0; index < divisionX; ++index)
  {
    table[index][6] = int(map(cos(radians(index * 90.0f)), -1.0f, 1.0f, 0.0f, 255.0f));
  }

  // 8. boucle croissante avec mapping selon une fonction trigonométrique (cosinus de 45 degrés par indice)
  for (index = 0; index < divisionX; ++index)
  {
    table[index][7] = int(map(cos(radians(index * 45.0f)), -1.0f, 1.0f, 0.0f, 255.0f));
  }

  // 9. boucle croissante avec valeurs aléatoires (distribution uniforme)
  for (index = 0; index < divisionX; ++index)
  {
    table[index][8] = int(random(255.0f));
  }

  // 10. boucle croissante avec valeurs aléatoires (fonction de bruit)
  for (index = 0; index < divisionX; ++index)
  {
    table[index][9] = int(noise(index) * 255.0f);
  }
}

void draw()
{
  // délai de quelques frames avant de lancer la boucle d'animation
  if (frame > 15)
  {
    ++shift;

    // boucle d'animation dans les indices en x du tableau
    if (shift >= divisionX)
      shift = 0;
  }

  // affichage du contenu du tableau sous forme d'une grille de rectangles colorés
  for (indexX = 0; indexX < divisionX; ++indexX)
  {
    for (indexY = 0; indexY < divisionY; ++indexY)
    {
      offsetX = indexX + shift;

      if (offsetX >= divisionX)
        offsetX -= divisionX;

      positionX = diameter * indexX;
      positionY = diameter * indexY;

      fill(table[offsetX][indexY]);
      rect(positionX, positionY, diameter, diameter);
    }
  }
  ++frame;
}
