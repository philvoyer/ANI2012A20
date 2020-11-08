# ANI2012A20/userSetup.py | Programmation Python avec Maya | coding=utf-8
# Exemple d'un script de configuration lancé au démarrage de Maya.
# Pour être exécuté, le fichier doit absolument s'appeler 'useSetup.py' et se trouver au bon emplacement :
#   Windows: <drive>:\Documents and Settings\<username>\My Documents\maya\<Version>\scripts
#   MacOSX:  ~/Library/Preferences/Autodesk/maya/<version>/scripts
#   Linux:   ~/maya/<version>/scripts

import os
import sys

# 1. définir des alias au niveau global
import maya.cmds as mc
import maya.mel as mm
import maya.utils as mu

# 2. ajouter un répertoire local à la liste des chemins d'accès (remplacer par un chemin qui existe sur votre ordinateur)
localScriptFolder = '/.../scripts'

if os.path.isdir(localScriptFolder):
  if not localScriptFolder in sys.path:
    sys.path.append(localScriptFolder)

# 3. un flag global qui permet de confirmer que le script 'userSetup.py' a été exécuté au complet sans problème
user_setup_done = True
