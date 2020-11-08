# ANI2012A20/sitecustomize.py | Programmation Python avec Maya | coding=utf-8
# Exemple d'un script de configuration lancé à l'initialisation de l'interpréteur Python, avant le démarrage de Maya.
# Pour être exécuté, le fichier doit absolument s'appeler 'sitecustomize.py' et se trouver au bon emplacement :
#   Windows: <drive>:\Program Files\Autodesk\Maya<Version>\Python\lib\site-packages
#   MacOSX:  Applications/Autodesk/maya<Version>/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python<version>/site-packages
#   Linux:   /usr/autodesk/maya/lib/python<version>/site-packages

import os
import sys

# 1. extraction des variables d'environnement 'HOME' et 'USER'
home = os.getenv('HOME')
user = os.getenv('USER')

# 2. ajouter le répertoire 'Desktop' à la liste des chemins d'accès où Maya peut accéder à des scripts Python
sys.path.append(
  os.path.join(
    home[:home.find(user)], user, 'Desktop'))

# 3. ajouter le répertoire 'Document' à la liste des chemins d'accès où Maya peut accéder à des scripts Python
sys.path.append(
  os.path.join(
    home[:home.find(user)], user, 'Document'))
