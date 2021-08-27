# TP3 - Temps de réaction

Jusqu'à maintenant notre IA réagit très rapidement et on s'apercoit que même en augmentant la vitesse de la balle, notre IA peut suivre la balle à une vitesse folle...

Cependant on va ajouter un temps de réaction à notre IA pour la rendre plus intéressante

![hint](/ressources/TP3/hint_help.jpg)

Pour réaliser le TP il y a une nouvelle classe ReactionTime qui est composé de deux variables, "reaction_time" qui représente le temps de réaction en millisecondes, et "start_register_tick" qui est une variable qui nous servira à enregistrer un moment T de la partie !

Il y a également deux fonctions

```py
def register_tick(self):
       self.start_ticks = pygame.time.get_ticks()

def paddle_can_react(self):
   # à compléter
```

La première fonction register_tick() permet d'enregistrer un moment T de la partie, cela sera important puisque lorsque la balle va toucher la raquette, on veut enregistrer ce moment.

la fonction paddle_can_react() sera à compléter ! La fonction retourne True si la raquette a dépassé son temps de réaction sinon renvoie False si le temps de réaction n'a toujours pas était atteint.
A noter que le temps de réaction est en millisecondes, vous êtes libre de changer par ce que vous souhaitez.

Une fois cela réalisé il faudra également changer l'ia qu'on a construit pour prendre en compte ce paramètre !

Ainsi il faudra ajouter un booléen "can_react" pour savoir si notre IA a dépassé le temps de réaction défini !

```py
def easy_ia(self,ball,can_react):
   #  à completer
```

A vous de jouer !
