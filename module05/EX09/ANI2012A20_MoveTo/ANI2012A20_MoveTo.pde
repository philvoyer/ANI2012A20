// ANI2012A20_MoveTo.pde
// Animation du déplacement d'une base orthonormale vers une position en parcourant une fraction de la distance à chaque mise à jour.

// paramètres
float easing = 0.05f;

float arrowWidth = 150.0f;
float arrowHeight = 15.0f;

float crossRadius  = 10.0f;

float probability = 0.005f;

int colorBack = 0;

// variables
Vector position;
Vector target;
Vector velocity;

void setup()
{
  size(512, 512);
  frameRate(60);
  rectMode(CORNER);

  position = new Vector();
  target = new Vector();
  velocity = new Vector();

  target.x = width / 2.0f;
  target.y = height / 2.0f;

  drawCross(target.x, target.y, crossRadius);
}

void draw()
{
  fade(32);

  velocity.x = (target.x - position.x) * easing;
  velocity.y = (target.y - position.y) * easing;

  position.x += velocity.x;
  position.y += velocity.y;

  drawBasis(position.x, position.y, arrowWidth, arrowHeight);

  if (mousePressed == true)
  {
    target.x = mouseX;
    target.y = mouseY;

    drawCross(target.x, target.y, crossRadius);
  }
  else
  {
    if (random(0.0f, 1.0f) < probability)
    {
      target.x = random(width);
      target.y = random(height);

      drawCross(target.x, target.y, crossRadius);
    }
  }
}

// fonction qui dessine une base orthonormale
void drawBasis(float x, float y, float w, float h)
{
  fill(255, 0, 0);
  drawArrow(x, y, w, h, 0);

  fill(0, 255, 0);
  drawArrow(x, y, w, h, -PI / 2.0f);

  drawOrigin(x, y, h*2);
}

// fonction qui dessine l'origine d'une base orthonormale
void drawOrigin(float x, float y, float radius)
{
  stroke(255, 255, 255);
  strokeWeight(radius);

  point(x, y);
}

// fonction qui dessine une flèche
void drawArrow(float x, float y, float w, float h, float angle)
{
  noStroke();

  pushMatrix();

  translate(x, y);
  rotate(angle);

  beginShape();
  vertex(0, h / 2.0f);
  vertex(w, h / 2.0f);
  vertex(w, h / 2.0f + h / 2.0f);
  vertex(w + h * 1.618f, 0);
  vertex(w, - (h / 2.0f + h / 2.0f));
  vertex(w, - h / 2.0f);
  vertex(0, - h / 2.0f);
  endShape(CLOSE);

  popMatrix();
}

// fonction qui dessine une croix
void drawCross(float x, float y, float radius)
{
  stroke(191, 0, 191);
  strokeWeight(radius);

  line(x - radius, y - radius, x + radius, y + radius);
  line(x + radius, y - radius, x - radius, y + radius);
}

void fade(float decay)
{
  rectMode(CORNER);
  noStroke();
  fill(colorBack, decay);
  rect(0, 0, width, height);
}
