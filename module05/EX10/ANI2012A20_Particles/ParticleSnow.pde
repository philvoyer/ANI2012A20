// ANI2012A20_Particles/ParticleSnow.pde
// Classe de type ParticleSnow, qui hérite de la classe ParticlePhysic.

class ParticleSnow extends ParticlePhysic
{
  final static float probabilitySpawn = 0.618f;

  ParticleSnow()
  {
    super();

    colorDiffuse = #FFFFFF;

    lifetime = 5.0f;

    mass = 1.0f;
    speed = 0.0f;
    speedMax = 5.0f;

    noise.set(0.01f, 0.0f, 0.0f);
  }

  void init()
  {
    super.init();

    ps.space.x = width;
    ps.space.y = 32;

    position.x = ps.origin.x + random(0.0f, 1.0f) * ps.space.x  - ps.space.x / 2.0f;
    position.y = 0 + random(0.0f, 1.0f) * ps.space.y;

    force.set(0.0f, 0.0f, 0.0f);
    acceleration.set(0.0f, 0.0f, 0.0f);
    velocity.set(0.0f, 0.0f, 0.0f);
    applyForce(0.0f, 1.0f, 0.0f);
  }

  void update()
  {
    applyForce(random(-noise.x, noise.x), 0.0f, 0.0f);
    super.update();
  }

  void render()
  {
    fill(colorDiffuse, 127);
    ellipse(position.x, position.y, 16, 16);
  }
}
