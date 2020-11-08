# ANI2012A20_Help.py | Programmation Python avec Maya | coding=utf-8
# Documentation sur les fonctions et commandes Python utilisées dans les exemples du cours.

import sys
import math
import maya
import maya.cmds

def doc_modules():
  """fonction qui affiche la documentation des principaux modules utilisés dans les exemples du cours"""

  print "\n<documentation des principaux modules utilisés dans les exemples du cours>"

  # module  'sys'
  print "\n<documentation du module 'sys'>\n"
  help(sys)

  # module  'math'
  print "\n<documentation du module 'math'>\n"
  help(math)

  # module  'maya'
  print "\n<documentation du module 'maya'>\n"
  help(maya)

  # module  'maya.cmds'
  print "\n<documentation du module 'maya.cmds'>\n"
  help(maya.cmds)

def doc_python_functions():
  """fonction qui affiche la documentation des principales fonctions Python utilisées dans les exemples du cours"""

  print "\n<documentation des principales fonctions python utilisées dans les exemples du cours>"

  # fonction python 'help'
  print "\n<documentation de la fonction 'help'>\n"
  help(help)

  # fonction python 'len'
  print "\n<documentation de la fonction 'len'>\n"
  help(len)

  # fonction python 'range'
  print "\n<documentation de la fonction 'range'>\n"
  help(range)

  # fonction python 'tuple'
  print "\n<documentation de la fonction 'tuple'>\n"
  help(tuple)

  # fonction python 'list'
  print "\n<documentation de la fonction 'list'>\n"
  help(list)

  # fonction python 'map'
  print "\n<documentation de la fonction 'map'>\n"
  help(map)

  # fonction python 'reduce'
  print "\n<documentation de la fonction 'reduce'>\n"
  help(reduce)

  # fonction python 'filter'
  print "\n<documentation de la fonction 'filter'>\n"
  help(filter)

def doc_maya_commands():
  """fonction qui affiche la documentation des principales commandes maya utilisées dans les exemples du cours"""

  print "\n<documentation des principales commandes maya utilisées dans les exemples du cours>\n"

  print "\n<documentation de la commande 'maya.cmds.help'>\n"
  print "%s" % maya.cmds.help('help')

  # commande maya 'ls'
  print "\n<documentation de la commande 'maya.cmds.ls'>\n"
  print "%s" % maya.cmds.help('ls')

  # commande maya 'select'
  print "\n<documentation de la commande 'maya.cmds.select'>\n"
  print "%s" % maya.cmds.help('select')

  # commande maya 'objExists'
  print "\n<documentation de la commande 'maya.cmds.objExists'>\n"
  print "%s" % maya.cmds.help('objExists')

  # commande maya 'getAttr'
  print "\n<documentation de la commande 'maya.cmds.getAttr'>\n"
  print "%s" % maya.cmds.help('getAttr')

  # commande maya 'setAttr'
  print "\n<documentation de la commande 'maya.cmds.setAttr'>\n"
  print "%s" % maya.cmds.help('setAttr')

  # commande maya 'connectAttr'
  print "\n<documentation de la commande 'maya.cmds.connectAttr'>\n"
  print "%s" % maya.cmds.help('connectAttr')

  # commande maya 'deleteAttr'
  print "\n<documentation de la commande 'maya.cmds.deleteAttr'>\n"
  print "%s" % maya.cmds.help('deleteAttr')

  # commande maya 'setKeyframe'
  print "\n<documentation de la commande 'maya.cmds.setKeyframe'>\n"
  print "%s" % maya.cmds.help('setKeyframe')

  # commande maya 'play'
  print "\n<documentation de la commande 'maya.cmds.play'>\n"
  print "%s" % maya.cmds.help('play')

  # commande maya 'playbackOptions'
  print "\n<documentation de la commande 'maya.cmds.playbackOptions'>\n"
  print "%s" % maya.cmds.help('playbackOptions')

  # commande maya 'currentTime'
  print "\n<documentation de la commande 'maya.cmds.currentTime'>\n"
  print "%s" % maya.cmds.help('currentTime')

  # commande maya 'xform'
  print "\n<documentation de la commande 'maya.cmds.xform'>\n"
  print "%s" % maya.cmds.help('xform')

def doc_modules():
  """fonction qui affiche la documentation des principaux modules utilisés dans les exemples du cours"""

  print "\n<documentation des principaux modules utilisés dans les exemples du cours>"

  # module  'sys'
  print "\n<documentation du module 'sys'>\n"
  help(sys)

  # module  'math'
  print "\n<documentation du module 'math'>\n"
  help(math)

  # module  'maya'
  print "\n<documentation du module 'maya'>\n"
  help(maya)

  # module  'maya.cmds'
  print "\n<documentation du module 'maya.cmds'>\n"
  help(maya.cmds)


print "\n<début de l'exécution>\n"

doc_python_functions()
doc_maya_commands()
# doc_modules() # en commentaire, car génère beaucoup de texte

print "\n<fin de l'exécution>\n"
