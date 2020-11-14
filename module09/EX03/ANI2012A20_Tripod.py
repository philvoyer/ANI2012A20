# ANI2012A20_Tripod.py | Programmation Python avec Maya | coding=utf-8
# Exemple de génération de la structure hiérarchique du squelette d'un personnage composé de plusieurs joints d'animation.
# Le personnage est un 'tripod', une créature dont le squelette a une tête et trois jambes.

# paramètres du programme
offset = 10
angle = 45
ratio = 0.618


# 1. création d'un joint d'animation connexe à aucun autre joint

# vider la sélection courante pour que le prochain joint soit une nouvelle racine hiérarchique
maya.cmds.select(deselect=True)

# création d'un joint à l'origine la scène
maya.cmds.joint(position=(0, 0, 0), name='Origin')


# 2. création d'une chaîne de joints d'animation pour la colonne du personnage et un point d'ancrage avec le sol

# vider la sélection courante pour que le prochain joint soit une nouvelle racine hiérarchique
maya.cmds.select(deselect=True)

# création de la racine hiérarchique du personnage (point d'ancrage)
maya.cmds.joint(position=(0, 0, 0), relative=True, name='Tripod')

# création d'un joint pour le bassin du personnage
maya.cmds.joint(position=(0, offset*ratio, 0), relative=True, name='TripodPelvis')

# création d'un joint pour la colonne du personnage
maya.cmds.joint(position=(0, offset*ratio**1, 0), relative=True, name='TripodSpine')

# création d'un joint pour le coup du personnage
maya.cmds.joint(position=(0, offset*ratio**2, 0), relative=True, name='TripodNeck')

# création d'un joint pour la tête du personnage
maya.cmds.joint(position=(0, offset*ratio**3, 0), relative=True, name='TripodHead')

# l'opérateur '**' est pour l'exponentiation, ex. x**y vaut dire x exposant y

# 3. création d'une chaîne de joints d'animation pour les jambes du personnage

# vider la sélection courante pour que le prochain joint soit une nouvelle racine hiérarchique
maya.cmds.select(deselect=True)

# liste des proportions de taille qui permettent de déterminer la position de chaque joint de la chaîne
listPosition = [0, offset*ratio, offset*ratio, offset*ratio, offset*ratio]

# liste des rotations qui permettent de déterminer l'angle entre chaque joint de la chaîne
listRotation = [0, angle, -angle, -angle, -angle]

# boucler sur chacune des trois jambes
for indexLeg in range(3):
  # boucler pour la génération des joints de chaque jambe
  for indexJoint in range(len(listPosition)):
    maya.cmds.joint(name='TripodLeg%s%s' % (indexLeg+1, indexJoint+1))
    maya.cmds.rotate(listRotation[indexJoint], rotateZ=True, relative=True, objectSpace=True)
    maya.cmds.move(listPosition[indexJoint], moveX=True, relative=True, objectSpace=True)
  # vider la sélection courante pour que le prochain joint soit une nouvelle racine hiérarchique
  maya.cmds.select(deselect=True)


# 4. transformation des trois jambes et connexion avec le reste du corps du personnage

# extraire la position du pelvis
positionPelvis = maya.cmds.xform('TripodPelvis', query=True, translation=True, worldSpace=True)

# assigner la position du pelvis à chacune des jambes
maya.cmds.xform('TripodLeg11', worldSpace=True, translation=positionPelvis)
maya.cmds.xform('TripodLeg21', worldSpace=True, translation=positionPelvis)
maya.cmds.xform('TripodLeg31', worldSpace=True, translation=positionPelvis)

# orienter les trois jambes
maya.cmds.xform('TripodLeg11', worldSpace=True, rotation=(0, 90, 0))
maya.cmds.xform('TripodLeg21', worldSpace=True, rotation=(0, 30*7, 0))
maya.cmds.xform('TripodLeg31', worldSpace=True, rotation=(0, 30*11, 0))

# connecter chacune des jambes au pelvis
maya.cmds.connectJoint('TripodLeg11', 'TripodPelvis', parentMode=True)
maya.cmds.connectJoint('TripodLeg21', 'TripodPelvis', parentMode=True)
maya.cmds.connectJoint('TripodLeg31', 'TripodPelvis', parentMode=True)
