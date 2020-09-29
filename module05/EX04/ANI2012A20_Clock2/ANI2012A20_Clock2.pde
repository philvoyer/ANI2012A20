// ANI2012A20_Clock2.pde
// Animation d'une horloge, version implémentée avec classe.

// paramètres
int fps = 60;

int colorBack = 31;

float speed = 1000.0f;  // vitesse accélérée (utiliser 1.0f pour vitesse normale)

float arrowWidth = 200.0f;
float arrowHeight = 20.0f;

// variable
Clock clock;

void setup()
{
  size(512, 512);
  frameRate(fps);

  clock = new Clock(width / 2.0f, height / 2.0f, fps, speed);
}

void draw()
{
  fade(2);

  clock.update();
  clock.render();
}

void fade(float decay)
{
  rectMode(CORNER);
  noStroke();
  fill(colorBack, decay);
  rect(0, 0, width, height);
}
