// ANI2012A20_Particles.pde
// Animation de différents systèmes de particules.

import java.util.Iterator;

// paramètres
int count = 500;

int colorBack = 0;

float probabilityChange = 0.001f;

// variables;

boolean isPSActive1 = false;
boolean isPSActive2 = false;
boolean isPSActive3 = false;
boolean isPSActive4 = false;

ParticleSystem ps1;
ParticleSystem ps2;
ParticleSystem ps3;
ParticleSystem ps4;

void setup()
{
  size(960, 540);
  frameRate(60);

  // instanciation d'un système de particules de type ParticleFirefly
  ps1 = new ParticleSystem(count, ParticleSystem.PARTICLE_TYPE_FIREFLY);

  // instanciation d'un système de particules de type ParticlePhysic
  ps2 = new ParticleSystem(count, ParticleSystem.PARTICLE_TYPE_PHYSIC);

  // instanciation d'un système de particules de type ParticleSnow
  ps3 = new ParticleSystem(count, ParticleSystem.PARTICLE_TYPE_SNOW);

  // instanciation d'un système de particules de type ParticleFlame
  ps4 = new ParticleSystem(count, ParticleSystem.PARTICLE_TYPE_FLAME);

  selectRandomSystem();
}

void draw()
{
  fade(32);

  if (isPSActive1)
    ps1.update();
  if (isPSActive2)
    ps2.update();
  if (isPSActive3)
    ps3.update();
  if (isPSActive4)
    ps4.update();

  if (mousePressed == true)
  {
    if (isPSActive1)
      ps1.add(mouseX, mouseY);
    if (isPSActive2)
      ps2.add(mouseX, mouseY);
    if (isPSActive3)
      ps3.add(mouseX, mouseY);
    if (isPSActive4)
      ps4.add(mouseX, mouseY);
  }

  if (random(0.0f, 1.0f) < probabilityChange)
    selectRandomSystem();
}

void selectRandomSystem()
{
  isPSActive1 = isPSActive2 = isPSActive3 = isPSActive4 = false;

  switch (int(random(1.0f, 5.0f)))
  {
    case 1:
      isPSActive1 = true;
      break;
    case 2:
      isPSActive2 = true;
      break;
    case 3:
      isPSActive3 = true;
      break;
    case 4:
      isPSActive4 = true;
      break;
  }
}

void keyReleased()
{
  if (key == '1')
    isPSActive1 = !isPSActive1;
  if (key == '2')
    isPSActive2 = !isPSActive2;
  if (key == '3')
    isPSActive3 = !isPSActive3;
  if (key == '4')
    isPSActive4 = !isPSActive4;
  if (key == ' ')
    saveFrame("render####.png");
}

void fade(float decay)
{
  rectMode(CORNER);
  noStroke();
  fill(colorBack, decay);
  rect(0, 0, width, height);
}
