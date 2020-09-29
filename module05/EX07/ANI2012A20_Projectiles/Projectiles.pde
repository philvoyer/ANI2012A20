// ANI2012A20_Projectiles/Projectile.pde
// Classe de type Projectile.

class Projectile
{
  float positionX;
  float positionY;

  float radius;

  boolean isActive;

  Projectile(){}

  void render()
  {
    if (isActive)
    {
      stroke(63, 0, 0);
      fill(191, 0, 0);
    }
    else
    {
      stroke(0, 63, 0);
      fill(0, 127, 0);
    }

    ellipse(positionX, positionY, radius, radius);
  }
}
