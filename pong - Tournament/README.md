# Tournoi IA

Vous pouvez faire des tournois contre des IA avec la version de ce jeu ! Un serveur est délivré et vous pouvez le lancer, un client est aussi délivré afin d'avoir des informations sur le tournois

## Guide

Tout d'abord installer pygame

```py
pip install pygame
```

Puis installer la librairie websockets

```py
pip install websockets
```

### 1 Lancer le serveur du tournoi

```py
cd pong game
python3 server.py
```

### 2 Lancer le client du tournoi

```py
cd pong game
python3 client.py
```

Vous avez une possibilité :

```
1 > Voir le classement actuel
```

### 3 Paramètrage du tournoi

Dans le fichier pong_py vous pouvez modifier deux paramètres

```py
NB_ROUND = 3 #Nombres de rounds total dans une partie
NB_POINT = 5 #Nombres de points dans une manche
SPEED_BALL=3 # Vitesse de la balle (lent = 0.5, normal=1.5, rapide=3)
SPEED_PADDLE=3 # Vitesse de la raquette (lent = 0.5, normal=1.5, rapide=3)
```

### 4 Créer ou choisissez une IA

Vous pourrez soit créer votre propre IA et modifier la fonction ou alors reprendre une des IA que vous avez créer lors des TPs comme par exemple ci-dessous l'IA qui prédit les mouvements de la balle.

```py
# Joueur 1
paddle1.advanced_ia(ball_direction, reaction_time.paddle_can_react())
paddle1.draw()

# Joueur 2
paddle2.advanced_ia(ball_direction, reaction_time.paddle_can_react())
paddle2.draw()
```

### 5 Lancer une partie

```py
python3 pong.py
```

Vous serez amené à tapez les deux noms des IA, le premier nom est l'IA qui se trouve à gauche, et le deuxième nom l'IA qui se trouve à droite.

Enfin appuyer sur P pour lancer la partie ! :)
