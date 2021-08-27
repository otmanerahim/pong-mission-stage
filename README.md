# TP Pong

Bienvenue dans les TP pour le jeu pong ! Durant ces TPs vous allez apprendre à créer des IA pour le jeu [Pong](https://fr.wikipedia.org/wiki/Pong) !

Avant de commencer les TPs il vous sera nécessaire de comprendre le code qui a été écrit par mes soins ! Ci-dessous se trouve une description des classes et leur rôles.

## Ball

La classe Ball est la classe permettant de gérer les mouvements de la balle, cependant vous n'aurez pas à la modifier

### Répresentation de la balle dans le jeu

La balle dans le jeu dans le jeu est représenté par une un vecteur de coordonnées (posX,posY), un rayon r et possède une vitesse de direction sur l'axe y et x nommé (dx,dy).

### CollisionManager

La classe CollisionManager est la classe permettant de gérer toutes les collisions du jeu

### PlayerScore

La classe PlayerScore permet de gérer le score des joueurs dans le jeu

### Paddle

La classe Paddle permet de gérer les mouvements des raquettes ! (Ca sera cette classe que vous devrez modifier dans les TPs :) )

### Répresentation de la raquette dans le jeu

La raquette dans le jeu est représenté par une un vecteur de coordonnées (posX,posY) et possède une vitesse de direction nommé sur l'axe y (dy).

Vous pouvez trouvez les différents TPs sur les liens ci-dessous.

- [TP1](TP1)
- [TP2](TP2)
- [TP3](TP3)
- [TP4](TP4)
- [TP5](TP5)

Sur chaque TP vous pourrez modifier la vitesse de la balle et celle de la raquette dans le fichier **pong.py**

```py
SPEED_BALL=3 # Vitesse de la balle (lent = 0.5, normal=1.5, rapide=3)
SPEED_PADDLE=3 # Vitesse de la raquette (lent = 0.5, normal=1.5, rapide=3)
```

## Lancement du jeu

Pour chaque TP il faut lancer le fichier pong.py

## Prérequis

python3

```py
pip install python3
```

librairie pygame

```py
pip install pygame
```
