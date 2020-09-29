// ANI2012A20_Particles/ParticlePhysic.pde
// Classe de type ParticlePhysic, qui hérite de la classe Particle.

class ParticlePhysic extends Particle
{
  final static float probabilitySpawn = 0.618f;

  Vector force;
  Vector acceleration;
  Vector velocity;
  Vector noise;

  float mass;
  float speed;
  float speedMax;

  ParticlePhysic()
  {
    super();

    colorDiffuse = #9900DD;

    lifetime = 5.0f;

    mass = 1.0f;
    speed = 0.0f;
    speedMax = 999.0f;

    force = new Vector(0.0f, 0.0f, 0.0f);
    acceleration = new Vector(0.0f, 0.0f, 0.0f);
    velocity = new Vector(0.0f, 0.0f, 0.0f);
    noise = new Vector(1.0f, 1.0f, 0.0f);
  }

  void init()
  {
    super.init();

    ps.space.x = width;
    ps.space.y = height;

    position.x = ps.origin.x + random(0.0f, 1.0f) * ps.space.x - ps.space.x / 2.0f;
    position.y = ps.origin.y + random(0.0f, 1.0f) * ps.space.y - ps.space.y / 2.0f;

    force.set(0.0f, 0.0f, 0.0f);
    acceleration.set(0.0f, 0.0f, 0.0f);
    velocity.set(0.0f, 0.0f, 0.0f);
    applyForce(random(-noise.x, noise.x), random(-noise.y, noise.y), 0.0f);
  }

  void update()
  {
    super.update();

    acceleration.set(
      force.x * timeElapsed,
      force.y * timeElapsed,
      force.z * timeElapsed);

    acceleration.divide(mass);

    velocity.add(acceleration);

    if (velocity.magnitude() > speedMax)
    {
      velocity.normalize();
      velocity.scale(speedMax);
    }

    if (position.y < height)
    {
      position.add(velocity);
    }
  }

  void render()
  {
    fill(colorDiffuse,127);
    ellipse(position.x, position.y, 16, 16);
  }

  void setVelocity(float x, float y, float z)
  {
    velocity.set(x, y, z);
    speed = velocity.magnitude();
  }

  void setAcceleration(float x, float y, float z)
  {
    acceleration.set(x, y, z);
    force.copy(acceleration);
    force.multiply(mass);
  }

  void setForce(float x, float y, float z)
  {
    force.set(x, y, z);
    acceleration.set(force.x, force.y, force.z);
    acceleration.divide(mass);
  }

  void applyForce(float x, float y, float z)
  {
    force.add(x, y, z);
  }

  void applyForce(Vector v)
  {
    force.add(v);
  }
}
