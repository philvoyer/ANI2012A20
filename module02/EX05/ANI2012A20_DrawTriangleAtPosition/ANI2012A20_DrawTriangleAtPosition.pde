// ANI2012A20_DrawTriangleAtPosition.pde
// Dessine un triangle équilatérale à une position précise.
// Le premier triangle est au centre de la fenêtre d'affichage.
// D'autres triangles peuvent être dessinés à la position d'un clic de souris.

// paramètre
float triangleEdgeSize = 200;

// variables
float positionTriangleX;
float positionTriangleY;

void setup()
{
  size(512, 512);
  strokeWeight(4);
  fill(127);

  // position initiale au centre de la fenêtre d'affichage
  positionTriangleX = width / 2.0f;
  positionTriangleY = height / 2.0f;
}

void draw()
{
  drawTriangle(positionTriangleX, positionTriangleY, triangleEdgeSize);
}

void drawTriangle(float x, float y, float edgeSize)
{
  float halfEdgeSize = edgeSize / 2.0f;

  float vertex1X = -halfEdgeSize;
  float vertex1Y =  halfEdgeSize;
  float vertex2X =  halfEdgeSize;
  float vertex2Y =  halfEdgeSize;
  float vertex3X =  0;
  float vertex3Y = -halfEdgeSize / 2 * sqrt(3.0f);

  triangle(
    vertex1X + x, vertex1Y + y,
    vertex2X + x, vertex2Y + y,
    vertex3X + x, vertex3Y + y);
}

void mouseReleased()
{
  positionTriangleX = mouseX;
  positionTriangleY = mouseY;
  triangleEdgeSize = random(10, 300);
  fill(int(random(256)), int(random(256)), int(random(256)));
}
