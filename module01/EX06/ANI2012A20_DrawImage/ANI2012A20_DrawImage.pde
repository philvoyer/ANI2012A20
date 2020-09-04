// ANI2012A20_DrawImage.pde
// Exemple d'importation et d'affichage d'une image cadrée sur la fenêtre.
// Le fichier image doit se trouver dans un répertoire appelé 'data' situé au même endroit que le fichier source

// déclaration d'une variable de type PImage pour référencer l'image
PImage img;

// fonction d'initialisation
void setup()
{
  // fenêtre d'affichage avec les mêmes dimensions que l'image
  size(512, 770);

  // importer l'image à partir du répertoire /data
  img = loadImage("gertie.jpg");
}

// fonction de mise à jour de l'affichage
void draw()
{
  // dessiner l'image à l'origine du système de coordonnées
  image(img, 0, 0);
}
