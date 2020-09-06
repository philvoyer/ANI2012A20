// ANI2012A20_Function4_Decay.pde
// Exemple d'utilisation d'une fonction pour générer l'animation d'un estompement progressif en pleine fenêtre.

// paramètre : couleur d'arrière-plan
int colorBack = 15;

// paramètre : niveau de transparence dans l'intervalle [0, 255]
float decay = 7;

void setup()
{
  size(960, 540);
  frameRate(60);
  background(255);
}

void draw()
{
  noStroke();

  // invocation de la fonction d'atténuation
  fade(decay);
}

// fonction qui atténue progressivement le contenu de la fenêtre
void fade(float decay)
{
  // couleur de remplissage de l'arrière-plan avec semi-transparence
  fill(colorBack, decay);

  // dessiner un rectangle qui recouvre toute la fenêtre
  rect(0, 0, width, height);
}

// réinitialiser la couleur de remplissage quand une touche du clavier est relâchée
void keyReleased()
{
  background(255);
}

// réinitialiser la couleur de remplissage lors d'un clic
void mouseReleased()
{
  background(255);
}
