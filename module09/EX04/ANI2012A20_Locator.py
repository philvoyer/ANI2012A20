# ANI2012A20_Locator.py | Programmation Python avec Maya | coding=utf-8
# Génération d'une représentation visuelle d'un localisateur à partir d'une arborescence de primitives géométriques (sphère, cylindre, cube).

print "\n<début de l'exécution>\n"

# paramètres du programme

# facteur de dimensionnement
scaleFactor = 1.0

# option pour système de coordonnées de main gauche ou droite (ex. Maya = main droite, Unity = main gauche)
isLeftHandedSystem = False

# option pour version en couleur des primitives (XYZ > RGB)
isInColor = True

# initialisation

# état logique en fonction du paramètre
isRightHandedSystem = not isLeftHandedSystem

print "\n<extraction de la transformation du premier objet sélectionné>\n"

# obtenir la liste des objets sélectionnés
selection = maya.cmds.ls(selection=True)

# valider s'il y a au moins un objet sélectionné
if len(selection) == 0:
  # transformation par défaut si aucun objet sélectionné
  selectionPosition = (0, 0, 0)
  selectionRotation = (0, 0, 0)
else:
  # aller chercher la position et l'orientation du premier objet de la liste des objets sélectionnés
  selectionPosition = maya.cmds.xform(selection[0], query=True, worldSpace=True, translation=True)
  selectionRotation = maya.cmds.xform(selection[0], query=True, worldSpace=True, rotation=True)


print "\n<création de la racine>\n"

# création d'un objet transformé dans l'espace, mais invisible qui sera utilisé comme racine de l'arborescence des composantes visuelles
basis = maya.cmds.spaceLocator(name='basis', position=(0, 0, 0))

# création d'une sphère qui symbolise l'origine de la base orthonormale
sphereRadius = scaleFactor
sphereResolutionX = 16
sphereResolutionY = 16

origin = maya.cmds.polySphere(name='basisOrigin', subdivisionsX=sphereResolutionX, subdivisionsY=sphereResolutionY, radius=sphereRadius*2)


print "\n<création des axes>\n"

# création de 3 cylindres qui symbolisent les axes X, Y et Z de la base orthonormale
cylindreResolution = 12
cylindreHeight = scaleFactor * 8
cylindreRadius = sphereRadius * 0.618

axisX = maya.cmds.polyCylinder(name='basisAxisX', subdivisionsAxis=cylindreResolution, radius=cylindreRadius, height=cylindreHeight)
axisY = maya.cmds.polyCylinder(name='basisAxisY', subdivisionsAxis=cylindreResolution, radius=cylindreRadius, height=cylindreHeight)
axisZ = maya.cmds.polyCylinder(name='basisAxisZ', subdivisionsAxis=cylindreResolution, radius=cylindreRadius, height=cylindreHeight)

# création de 3 cônes qui symbolisent la direction positive des axes X, Y et Z de la base orthonormale
coneResolution = 12
coneRadius = sphereRadius
coneHeight = coneRadius * 3

arrowX = maya.cmds.polyCone(name='basisArrowX', subdivisionsAxis=coneResolution, radius=coneRadius, height=coneHeight)
arrowY = maya.cmds.polyCone(name='basisArrowY', subdivisionsAxis=coneResolution, radius=coneRadius, height=coneHeight)
arrowZ = maya.cmds.polyCone(name='basisArrowZ', subdivisionsAxis=coneResolution, radius=coneRadius, height=coneHeight)


print "\n<construction de la structure hiérarchique>\n"

# mise en hiérarchie des différentes composantes à partir de la racine (ordre: enfant > parent, de la racine jusqu'aux feuilles de l'arborescence)
maya.cmds.parent(origin[0], basis[0])
maya.cmds.parent(axisX[0], "%s|%s" % (basis[0], origin[0]))
maya.cmds.parent(axisY[0], "%s|%s" % (basis[0], origin[0]))
maya.cmds.parent(axisZ[0], "%s|%s" % (basis[0], origin[0]))
maya.cmds.parent(arrowX[0], "%s|%s|%s" % (basis[0], origin[0], axisX[0]))
maya.cmds.parent(arrowY[0], "%s|%s|%s" % (basis[0], origin[0], axisY[0]))
maya.cmds.parent(arrowZ[0], "%s|%s|%s" % (basis[0], origin[0], axisZ[0]))

# références sur les noeuds de transformation dans la hiérarchie
basisTransform = basis[0]

originTransform = "%s|%s" % (basis[0], origin[0])

axisXTransform = "%s|%s|%s" % (basis[0], origin[0], axisX[0])
axisYTransform = "%s|%s|%s" % (basis[0], origin[0], axisY[0])
axisZTransform = "%s|%s|%s" % (basis[0], origin[0], axisZ[0])

arrowXTransform = "%s|%s|%s|%s" % (basis[0], origin[0], axisX[0], arrowX[0])
arrowYTransform = "%s|%s|%s|%s" % (basis[0], origin[0], axisY[0], arrowY[0])
arrowZTransform = "%s|%s|%s|%s" % (basis[0], origin[0], axisZ[0], arrowZ[0])

# calcul des distances relatives au parent
translationAxis = cylindreHeight/2 + sphereRadius/2
translationArrow = cylindreHeight/2 + coneHeight/2

# translation des cônes (direction de l'axe) par rapport aux cylindres (axes)
maya.cmds.xform(arrowXTransform, objectSpace=True, translation=(0, translationArrow, 0))
maya.cmds.xform(arrowYTransform, objectSpace=True, translation=(0, translationArrow, 0))
maya.cmds.xform(arrowZTransform, objectSpace=True, translation=(0, translationArrow, 0))

# rotation des cylindres (axes)
maya.cmds.xform(axisXTransform, worldSpace=True, rotation=(0, 0 , -90))

# déterminer la direction de l'axe Z selon le type de système de coordonnées
if isLeftHandedSystem:  # la direction de l'axe Z est positive
  maya.cmds.xform(axisZTransform, worldSpace=True, rotation=(-90, 0, 0))
elif isRightHandedSystem: # la direction de l'axe Z est négative
  maya.cmds.xform(axisZTransform, worldSpace=True, rotation=( 90, 0, 0))

# translation des cylindres (axes) par rapport à la sphère (origine)
maya.cmds.xform(axisXTransform, worldSpace=True, translation=(translationAxis, 0, 0))
maya.cmds.xform(axisYTransform, worldSpace=True, translation=(0, translationAxis, 0))

# l'orientation de l'axe Z dépend du type de système de coordonnées (main gauche ou main droite)
if isLeftHandedSystem:
  maya.cmds.xform(axisZTransform, worldSpace=True, translation=(0, 0, -translationAxis))
elif isRightHandedSystem:
  maya.cmds.xform(axisZTransform, worldSpace=True, translation=(0, 0,  translationAxis))


print "\n<transformation de la structure>\n"

# transformation de la racine de la hiérarchie à la position et l'orientation de l'objet sélectionné ou sinon à l'origine de la scène.
maya.cmds.xform(basisTransform, worldSpace=True, translation=selectionPosition, rotation=selectionRotation)

# coloration des sommets des primitives géométriques
if isInColor:

  print "\n<coloration de la structure>\n"

  color = [0.618, 0.618, 0.618]
  maya.cmds.polyColorPerVertex(originTransform, colorRGB=color, colorDisplayOption=True)

  color = [1.0, 0.0, 0.0]
  maya.cmds.polyColorPerVertex(axisXTransform,  colorRGB=color, colorDisplayOption=True)
  maya.cmds.polyColorPerVertex(arrowXTransform, colorRGB=color, colorDisplayOption=True)

  color = [0.0, 1.0, 0.0]
  maya.cmds.polyColorPerVertex(arrowYTransform, colorRGB=color, colorDisplayOption=True)
  maya.cmds.polyColorPerVertex(axisYTransform,  colorRGB=color, colorDisplayOption=True)

  color = [0.0, 0.0, 1.0]
  maya.cmds.polyColorPerVertex(axisZTransform,  colorRGB=color, colorDisplayOption=True)
  maya.cmds.polyColorPerVertex(arrowZTransform, colorRGB=color, colorDisplayOption=True)


print "\n<fin de l'exécution>\n"
