// ANI2012A20_Henon.pde
// Animation d'un système chaotique de type attracteur de Henon

// paramètres
int count = 100;

int strokeSize = 4;

float frequency = 100.0f;

float timeThreshold = 3000.0f;

// variables
float centerX;
float centerY;

int index;

float angle;
float cosinus;
float sinus;

float offset;

float timeLast;
float timeElapsed;

Henon[] list;

void setup()
{
  size(512, 512);

  centerX = width / 2.0f;
  centerY = height / 2.0f;

  strokeWeight(strokeSize);

  timeElapsed = 0.0f;
  timeLast = millis();

  reset();
}

// fonction d'initialisation du système chaotique
void reset()
{
  angle = random(TWO_PI);

  cosinus = cos(angle);
  sinus = sin(angle);

  offset = 1.0f / count;

  // création d'une liste des éléments de l'attracteur
  list = new Henon[count];

  // initialisation
  for (index = 0; index < count; ++index)
    list[index] = new Henon(index * offset, noise(index * 0.05f));

  // couleur aléatoire
  stroke(
    (int) random(256.0f),
    (int) random(256.0f),
    (int) random(256.0f),
    191);

  strokeWeight(strokeSize);

  background(31);
}

void draw()
{
  timeElapsed += (millis() - timeLast);
  timeLast = millis();

  // réinitialiser le système après un certain temps
  if (timeElapsed >= timeThreshold)
  {
    timeElapsed -= timeThreshold;
    reset();
  }

  // mise à jour de la position des éléments de l'attracteur
  for (index = 0; index < count; ++index)
    list[index].update();

  // dessiner les éléments de l'attracteur
  for (index = 0; index < count; ++index)
    list[index].render();
}

void keyReleased()
{
  if (keyCode == UP)
    strokeSize += 1;
  if (keyCode == DOWN)
    strokeSize = --strokeSize > 1 ? strokeSize : 1;

  strokeSize = int(random(1.0f, 8.0f));

  println("stroke size : " + strokeSize);

  reset();
}

void mouseReleased()
{
  strokeSize = int(random(1.0f, 8.0f));
  reset();
}
