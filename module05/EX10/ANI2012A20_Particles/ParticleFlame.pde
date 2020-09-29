// ANI2012A20_Particles/ParticleFlame.pde
// Classe de type ParticleFlame, qui hérite de la classe ParticlePhysic.

class ParticleFlame extends ParticlePhysic
{
  final static float probabilitySpawn = 0.9f;

  color colorFinal;

  ParticleFlame()
  {
    super();

    colorDiffuse = #FFFF40;
    colorFinal   = #FF6600;

    lifetime = 3.5f;

    mass = 0.5f;
    speed = 0.0f;
    speedMax = 1.0f;

    noise.set(0.05f, 0.0f, 0.0f);
  }

  void init()
  {
    super.init();

    ps.space.x = width;
    ps.space.y = 32;

    position.x = ps.origin.x + random(0.0f, 1.0f) * ps.space.x  - ps.space.x / 2.0f;
    position.y = height - random(0.0f, 1.0f) * ps.space.y;

    force.set(0.0f, 0.0f, 0.0f);
    acceleration.set(0.0f, 0.0f, 0.0f);
    velocity.set(0.0f, 0.0f, 0.0f);
    applyForce(0.0f, -0.5f, 0.0f);
  }

  void update()
  {
    applyForce(random(-noise.x, noise.x), 0.0f, 0.0f);
    super.update();
  }

  void render()
  {
    fill(
      lerpColor(colorDiffuse, colorFinal, timeActive / (lifetime * 1000.0f)),
      int(map(timeActive, 0.0f, lifetime * 1000.0f, 192.0f, 0.0f)));

    ellipse(
      position.x,
      position.y,
      int(map(timeActive, 0.0f, lifetime * 1000.0f, 16.0f, 64.0f)),
      int(map(timeActive, 0.0f, lifetime * 1000.0f, 16.0f, 64.0f)));
  }
}
