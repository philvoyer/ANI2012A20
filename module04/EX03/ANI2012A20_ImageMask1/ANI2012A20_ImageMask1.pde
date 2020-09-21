// ANI2012A20_ImageMask1.pde
// Exemple d'application d'un masque (échiquier) sur une image (dégradé).

// paramètres
String fileSource = "imgSource.png";
String fileMask = "imgMask.png";

// variables
PImage imgSource;

PImage imgMask;

void setup()
{
  size(512, 512);

  // charger les images en mémoires
  imgSource = loadImage(fileSource);
  imgMask = loadImage(fileMask);
}

void draw()
{
  // couleur d'arrière-plan
  background(0, 191, 0);

  // appliquer le masque sur l'image source
  imgSource.mask(imgMask);

  // dessiner l'image masquée
  image(imgSource, 0, 0);
}
