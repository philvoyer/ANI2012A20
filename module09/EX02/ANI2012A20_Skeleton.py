# ANI2012A20_Skeleton.py | Programmation Python avec Maya | coding=utf-8
# Exemple de manipulations de listes contentant les noms de différents joints d'animation d'un bipède.

print "\n<début de l'exécution>\n"


# 1. déclaration des liste de types de joint

print "\n<ex1. création d'une liste pour chaque type de joint du squelette>\n"

# liste des joints de la tête
listJointHead = ['Neck', 'Head']

# liste des joints du torse
listJointTorso = ['Pelvis', 'Spine1', 'Spine2', 'Spine3']

# liste des joints d'un bras
listJointArm = ['Hand', 'Elbow', 'Shoulder']

# liste des joints d'une jambe
listJointLeg = ['Hip', 'Knee', 'Foot']

print "<listes des membres du squelette>\n"

print "<liste des joints de la tête : " + str(listJointHead) + ">"
print "<liste des joints du torse : " + str(listJointTorso) + ">"
print "<liste des joints des bras : " + str(listJointArm) + ">"
print "<liste des joints des jambes : " + str(listJointLeg) + ">\n"


# 2. variation des listes de types de joint

print "\n<ex2. créer des variations des listes de joints (bras gauche et bras droit, jambe gauche et jambe droite)>\n"

# création de quelques listes vides
listJointArmLeft = []
listJointArmRight = []
listJointLegLeft = []
listJointLegRight = []

# remplir les listes et éditer le nom des joints pour rajouter un suffixe pour le côté gauche ou droit

for joint in listJointArm:
  listJointArmLeft.append ('Left' + joint)
  listJointArmRight.append('Right' + joint)

print "<liste des joints du bras gauche et droit>\n"
print "<liste des joints du bras gauche : " + str(listJointArmLeft) + ">"
print "<liste des joints du bras droit : " + str(listJointArmRight) + ">\n"

for joint in listJointLeg:
  listJointLegLeft.append ('Left' + joint)
  listJointLegRight.append('Right' + joint)

print "<liste des joints de la jambe gauche et droite>\n"
print "<liste des joints de la jambe gauche : " + str(listJointLegLeft) + ">"
print "<liste des joints de la jambe droite : " + str(listJointLegRight) + ">\n"


# 3. fusion des listes de types de joint

print "\n<ex3. fusion des listes dans une seule liste>\n"

# fusion de toutes les listes de joints en une seule liste
listSkeleton = listJointHead + listJointTorso + listJointArmLeft + listJointArmRight + listJointLegLeft + listJointLegRight

print "<liste de tous les joints du squelette : " + str(listSkeleton) + ">\n"


# 4. création des joints

print "\n<ex4. création des joints du squelette>\n"

# parcourir la liste des joints du squelette et crée des instances de chaque type de joint
for index in range(len(listSkeleton)):
  maya.cmds.joint(name='%s' % listSkeleton[index])
  maya.cmds.select(deselect=True) # pour éviter que le joint soit connecté au précédent

# à ce stade, les joints ne sont ni transformés ni connectés, ils sont seulement instanciés dans la scène


print "\n<fin de l'exécution>\n"
