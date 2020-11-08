# ANI2012A20_Playback.py | Programmation Python avec Maya | coding=utf-8
# Exemples de manipulations des propriétés de lecture des animations.

print "\n<début de l'exécution>\n"


# 1. extraire le temps d'animation courant

print "<ex1>"

def animation_time_current():
  """fonction qui retourne le temps d'animation courant"""

  return maya.cmds.currentTime(query=True)

timestamp = animation_time_current()

print "<temps d'animation courant : %s>\n" % timestamp


# 2. sauter directement à un frame d'une animation

print "<ex2>"

def animation_time_jump_to(timeframe):
  """fonction qui permet de sauter directement à frame d'une animation"""

  print "<aller au frame d'animation : %s>" % timeframe

  maya.cmds.currentTime(timeframe, edit=True)

animation_time_jump_to(10);

timestamp = animation_time_current()

print "<frame d'animation courant : %s>\n" % timestamp


# 3. marqueur de début d'animation

print "<ex3>"

def animation_sequence_marker_start(timeframe):
  """fonction qui configure le marqueur de début d'animation"""

  maya.cmds.playbackOptions(animationStartTime=timeframe, edit=True)

animation_sequence_marker_start(0)

timestamp = maya.cmds.playbackOptions(query=True, animationStartTime=True)

print "<marqueur de début d'animation : %s>\n" % timestamp


# 4. marqueur de fin d'animation

print "<ex4>"

def animation_sequence_marker_end(timeframe):
  """fonction qui configure le marqueur de fin d'animation"""

  maya.cmds.playbackOptions(edit=True, animationEndTime=timeframe)

animation_sequence_marker_end(48)

timestamp = maya.cmds.playbackOptions(query=True, animationEndTime=True)

print "<marqueur de fin d'animation : %s>\n" % timestamp


# 5. marqueur de début de lecture

print "<ex5>"

def animation_playback_marker_start(timeframe):
  """fonction qui configure le marqueur de début de lecture"""

  maya.cmds.playbackOptions(edit=True, minTime=timeframe)

animation_playback_marker_start(12)

timestamp = maya.cmds.playbackOptions(query=True, minTime=True)

print "<marqueur de début de lecture : %s>\n" % timestamp


# 6. marqueur de fin de lecture

print "<ex6>"

def animation_playback_marker_end(timeframe):
  """fonction qui configure le marqueur de fin de lecture"""

  maya.cmds.playbackOptions(edit=True, maxTime=timeframe)

animation_playback_marker_end(24)

timestamp = maya.cmds.playbackOptions(query=True, maxTime=True)

print "<marqueur de fin de lecture : %s>\n" % timestamp


# 7. configuration du comportement de lecture en fin d'animation

print "<ex7>"

def animation_playback_loop_once():
  """fonction qui configure le comportement de lecture en fin d'animation à l'option 'once'"""

  maya.cmds.playbackOptions(edit=True, loop='once')

def animation_playback_loop_continuous():
  """fonction qui configure le comportement de lecture en fin d'animation à l'option 'continuous'"""

  maya.cmds.playbackOptions(edit=True, loop='continuous')

def animation_playback_loop_oscillate():
  """fonction qui configure le comportement de lecture en fin d'animation à l'option 'oscillate'"""

  maya.cmds.playbackOptions(edit=True, loop='oscillate')

animation_playback_loop_once()

print "<comportement de fin d'animation : %s>"   % maya.cmds.playbackOptions(query=True, loop=True)

animation_playback_loop_continuous()

print "<comportement de fin d'animation : %s>"   % maya.cmds.playbackOptions(query=True, loop=True)

animation_playback_loop_oscillate()

print "<comportement de fin d'animation : %s>\n" % maya.cmds.playbackOptions(query=True, loop=True)


# 8. nombre de frames par seconde

print "<ex8>"

def frames_per_second():
  """fonction qui retourne le nombre de frames par seconde"""

  return maya.cmds.playbackOptions(query=True, framesPerSecond=True)

fps = frames_per_second()

print "<nombre de frames par seconde : %s>\n" % fps


# 9. vitesse de lecture

print "<ex9>"

def animation_playback_speed(speed):
  """fonction qui configure la vitesse de lecture"""

  maya.cmds.playbackOptions(edit=True, playbackSpeed=speed)

animation_playback_speed(2) # 200%

speed = maya.cmds.playbackOptions(query=True, playbackSpeed=True)

print "<vitesse de lecture : %s>" % speed

animation_playback_speed(0.5) # 50%

speed = maya.cmds.playbackOptions(query=True, playbackSpeed=True)

print "<vitesse de lecture : %s>" % speed

animation_playback_speed(1) # 100% (valeur par défaut)

speed = maya.cmds.playbackOptions(query=True, playbackSpeed=True)

print "<vitesse de lecture : %s>\n" % speed


# 10. vitesse de lecture maximale

print "<ex10>"

def animation_playback_speed_max(speed):
  """fonction qui configure la vitesse de lecture maximale"""

  maya.cmds.playbackOptions(edit=True, maxPlaybackSpeed=speed)

animation_playback_speed_max(1)

speed = maya.cmds.playbackOptions(query=True, maxPlaybackSpeed=True)

print "<vitesse de lecture maximale : %s>" % speed

animation_playback_speed_max(24)

speed = maya.cmds.playbackOptions(query=True, maxPlaybackSpeed=True)

print "<vitesse de lecture maximale : %s>\n" % speed


# 11. valeur d'incrémentation d'une image à l'autre

print "<ex11>"

def animation_frame_increment(step):
  """fonction qui configure la valeur d'incrémentation d'une image à l'autre"""

  maya.cmds.playbackOptions(edit=True, by=step)

animation_frame_increment(3)

increment = maya.cmds.playbackOptions(query=True, by=True)

print "<valeur d'incrémentation des frames : %s>" % increment

animation_frame_increment(1) # valeur par défaut

increment = maya.cmds.playbackOptions(query=True, by=True)

print "<valeur d'incrémentation des frames : %s>\n" % increment


# 12. mise à jour des fenêtres d'affichage

print "<ex12>"

def animation_view_update_all():
  """fonction qui configure le mode de mise à jour des fenêtres d'affichage à l'option 'all'"""

  maya.cmds.playbackOptions(edit=True, view='all')

def animation_view_update_active():
  """fonction qui configure le mode de mise à jour des fenêtres d'affichage à l'option 'active'"""

  maya.cmds.playbackOptions(edit=True, view='active')

animation_view_update_all()

print u"<mode de mise à jour des fenêtres d'affichage : %s>" % maya.cmds.playbackOptions(query=True, view=True)

animation_view_update_active()

print u"<mode de mise à jour des fenêtres d'affichage : %s>\n" % maya.cmds.playbackOptions(query=True, view=True)


# 13. contrôle de la lecture d'une animation

print "<ex13>"

def animation_play_forward():
  """fonction qui lance la lecture de l'animation du marqueur de début jusqu'au marqueur de fin"""

  print "<animation play forward>"
  maya.cmds.play(forward=True)

def animation_play_backward():
  """fonction qui lance la lecture de l'animation du marqueur de fin jusqu'au marqueur de début"""

  print "<animation play backward>"
  maya.cmds.play(forward=False)

def animation_stop():
  """fonction qui arête la lecture de l'animation"""

  print "<animation stop>"
  maya.cmds.play(state=False)

def animation_is_playing():
  """fonction qui retourne vrai si l'animation est en train de jouer et faux sinon"""

  return maya.cmds.play(query=True, state=True)

def animation_recording():
  """fonction qui active le mode d'enregistrement pendant une boucle d'animation"""

  print "<animation recording>"
  maya.cmds.play(record=True)

# lancer la lecture de l'animation
animation_play_forward()

# valider que l'animiation est en cours de lecture
if animation_is_playing():
  print "<la lecture de l'animation est active>"

# arrêter l'animation
animation_stop()

print "\n<fin de l'exécution>\n"
