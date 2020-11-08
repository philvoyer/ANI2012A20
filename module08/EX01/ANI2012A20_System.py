# ANI2012A20_System.py | Programmation Python avec Maya | coding=utf-8
# Exemples de scripts qui permettent d'extraire de l'information sur le système hôte.

import os
import sys
import platform
import maya.cmds
import maya.utils

print "\n<début de l'exécution>\n"


# 1. système d'exploitation

print "\n<déterminer quel est le système d'exploitation>\n"

if os.name == 'posix':
  print "\n<os : posix (linux ou macos)>"
else:
  print "\n<os : windows>"


# 2. versions de l'environnement

print "\n<information sur les versions de l'environnement où le script est exécuté>\n"

print "\n<system version: sys.version>"
print "%s" % sys.version

print "\n<system version: sys.version_info>"
print "%s" % sys.version_info


# 3. analyse du système

print "\n<informations sur le système hôte où le script est exécuté>\n"

def system_analysis():
  """fonction qui analyse le système hôte"""
  print "\n<system analysis>"
  print "\tos:        %s" % os.name
  print "\tmachine:   %s" % platform.machine()
  print "\tprocessor: %s" % platform.processor()
  print "\tsystem:    %s" % platform.system()
  print "\trelease:   %s" % platform.release()
  print "\tversion:   %s" % platform.version()
  print "\tnode:      %s" % platform.node()
  print "<system analysis>"

system_analysis()


# 4. délimiteur de chemin d'accès

print "\n<déterminer quel est le délimiteur de chemin d'accès en fonction du système d'exploitation>\n"

if os.name == 'posix': # macos & linux
  delimitor = ':'
else:                  # windows
  delimitor = ';'

print "\n<delimitor: '%s'>" % delimitor


# 5. variables d'environnement

# afficher le contenu de la variable d'environnement 'MAYA_SCRIPT_PATH' (répertoires où les scripts MEL sont accessibles)

print "\n<variable d'environnement: 'MAYA_SCRIPT_PATH'>"

for path in os.getenv("MAYA_SCRIPT_PATH").split(delimitor):
  print "\t%s" % path

print "<variable d'environnement>"

# afficher le contenu de la variable d'environnement 'PYTHONPATH' (répertoires où les scripts Python sont accessibles)

print "\n<variable d'environnement: 'PYTHONPATH'>"

for path in os.getenv("PYTHONPATH").split(delimitor):
  print "\t%s" % path

print "<variable d'environnement>"


# 6. chemins d'accès

print "\n<afficher les chemins d'accès utilisés par Maya>"

print "\n<maya path>"
print "\t%s" % maya.cmds.internalVar(userAppDir=True)
print "\t%s" % maya.cmds.internalVar(userScriptDir=True)
print "\t%s" % maya.cmds.internalVar(userPrefDir=True)
print "\t%s" % maya.cmds.internalVar(userPresetsDir=True)
print "\t%s" % maya.cmds.internalVar(userShelfDir=True)
print "\t%s" % maya.cmds.internalVar(userMarkingMenuDir=True)
print "\t%s" % maya.cmds.internalVar(userBitmapsDir=True)
print "\t%s" % maya.cmds.internalVar(userTmpDir=True)
print "\t%s" % maya.cmds.internalVar(userWorkspaceDir=True)
print "<maya path>"

print "\n<afficher la liste des chemins d'accès du système>"

def print_system_paths():
  """fonction qui affiche la liste des chemins d'accès du système"""

  print "\n<system path>"

  for path in sys.path:
    print "\t%s" % path

  print "<system path>"

print_system_paths()


# 7. symboles

print "\n<afficher la liste des symboles de portée globale du système>\n"

def print_global_symbols():
  """affiche la liste des symboles avec définition de portée globale"""

  print "\n<global symbols>"

  for symbol in globals().keys():
    print "\t%s" % symbol

  print "<global symbols>"

print_global_symbols()


print "\n<fin de l'exécution>\n"
