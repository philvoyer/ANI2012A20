// ANI2012A20_Function2_Random.pde
// Exemples de génération de nombres pseudo-aléatoires.

// variables
int intMin;
int intMax;

int intRandomNumber;

float floatMin;
float floatMax;

float floatRandomNumber;

void setup()
{
  // mise à jour une fois par seconde
  frameRate(1);

  // valeur initiale du germe (seed) de l'algorithme de génération de nombres pseudo-aléatoires
  randomSeed(millis());

  // valeur initiale du germe (seed) de l'algorithme de bruit de Perlin
  noiseSeed(millis());

  // la fonction millis() retourne le nombre de millisecondes écoulées depuis le lancement du programme
  // puisque sa valeur est différente à chaque mise à jour du programme,
  // cela en fait un bon germe pour la génération de nombres pseudo-aléatoires
}

void draw()
{
  println("\nrandom number generation :");

  // 1. génération d’un nombre aléatoire dans l'intervalle [0, 1[
  floatRandomNumber = random(0.0f, 1.0f);

  println("1: random [0.0, 1.0[ = " + floatRandomNumber);

  // 2. génération d’un nombre aléatoire réel (float) dans l'intervalle [min, max[
  floatMin = 3;
  floatMax = 6;

  floatRandomNumber = floatMin + random(floatMax - floatMin);

  println("2: random [" + floatMin + ", " + floatMax + "[ = " + floatRandomNumber);

  // 3. génération d’un nombre aléatoire entier (int) dans l'intervalle [min, max]
  intMin = 3;
  intMax = 6;

  intRandomNumber = intMin + int(random(intMax - intMin + 1));

  println("3: random [" + intMin + "  , " + intMax + "  ] = " + intRandomNumber);

  // 4. génération d’un nombre aléatoire dans l'intervalle [0, 1[.
  floatRandomNumber = noise(millis());

  println("4: noise  [0  , 1  [ = " + floatRandomNumber);
}
