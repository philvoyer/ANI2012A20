// ANI2012A20_DrawText.pde
// Affiche le sigle du cours au centre de la fenêtre d'affichage.

// fonction qui configure la largeur et la hauteur de la fenêtre d'affichage
size(256, 256);

// fonction qui configure la couleur du texte
fill(255, 127, 63);

// fonction qui configure l'alignement du texte
textAlign(CENTER);

// fonction qui configure la taille du texte
textSize(32);

// fonction pour afficher du texte (premier paramètre) à une position X (second paramètre) et Y (troisième paramètre)
text("ANI-2012", width / 2, height / 2);
