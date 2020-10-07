// ANI2012A20_KochSnowflake.pde
// Génération d'un système fractal de type flocon de Koch.

// paramètres
int depthCurrent = 3;
int depthMax = 8;

float offset = 200.0f;

// variables
ArrayList<Koch> kochListDraw;
ArrayList<Koch> kochListNext;

Vector v1;
Vector v2;
Vector v3;

void setup()
{
  size(512, 512);
  noLoop();
  noFill();

  // instancier et initialiser les positions des sommets du triangle
  v1 = new Vector(offset, 0.0f, 0.0f);
  v2 = new Vector(-offset, 0.0f, 0.0f);
  v3 = new Vector(0.0f, offset * sqrt(3.0f), 0.0f);

  // invocation de la fonction qui génère la forme fractale
  generate();
}

void draw()
{
  background(255);

  // ajustement de la caméra
  scale(1.0f, -1.0f);
  translate(0.0f, -height);
  translate(width / 2.0f, 0.0f);
  translate(0.0f, height / 4.0f);

  stroke(223);
  strokeWeight(1);

  // dessiner le triangle d'origine
  triangle(
   v1.x, v1.y,
   v2.x, v2.y,
   v3.x, v3.y);

  stroke(31);
  strokeWeight(3);

  // dessiner les segments de la forme fractale
  for (Koch segment : kochListDraw)
    segment.render();
}

// fonction qui génère la forme fractale de Koch
void generate()
{
  // instancier la liste qui contient les segments de la forme fractale
  kochListDraw = new ArrayList<Koch>();

  // ajouter le segment à la liste
  kochListDraw.add(new Koch(v2, v1));
  kochListDraw.add(new Koch(v3, v2));
  kochListDraw.add(new Koch(v1, v3));

  // invocation de la fonction qui sous-divise la forme fractale
  for (int index = 0; index < depthCurrent; ++index)
    subdivide();

  println("current depth : " + depthCurrent);
}

// fonction qui sous-divise une ligne selon le principe de la forme fractale de Koch (pattern : ._./.\._.)
void subdivide()
{
  // instancier une nouvelle liste vide
  kochListNext = new ArrayList<Koch>();

  // pour chaque segment de la forme fractale (ligne)
  for (Koch segment : kochListDraw)
  {
    // calculer la position des cinq nouveaux points
    Vector position1 = segment.computePosition1();
    Vector position2 = segment.computePosition2();
    Vector position3 = segment.computePosition3();
    Vector position4 = segment.computePosition4();
    Vector position5 = segment.computePosition5();

    // créer les quatre nouvelles sous-divisions
    kochListNext.add(new Koch(position1, position2));
    kochListNext.add(new Koch(position2, position3));
    kochListNext.add(new Koch(position3, position4));
    kochListNext.add(new Koch(position4, position5));
  }

  // la nouvelle liste devient la liste courante
  kochListDraw = kochListNext;
}

void keyReleased()
{
  if (keyCode == UP)
  {
    depthCurrent = ++depthCurrent < depthMax ? depthCurrent : depthMax;
    generate();
  }
  if (keyCode == DOWN)
  {
    depthCurrent = --depthCurrent > 0 ? depthCurrent : 0;
    generate();
  }

  // redessiner la scène
  redraw();
}
