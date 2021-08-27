# TP4 - Prédiction de la balle

Ce TP est à faire en deux parties, vous ne pourrez pas faire la deuxième partie si la première n'est pas réalisée.

Il est maintenant temps de passer aux choses sérieuses ! Jusqu'à maintenant la vitesse de la balle était toujours inférieur à celle de la raquette, cependant on va modifier ce paramètre pour que la vitesse de la balle soit supérieur à celle de la raquette ! Et oui notre IA est pour l'instant basé sur le suivi de la balle, cependant il ne pourra plus suivre la balle si celle-ci est trop rapide !

Il faudra donc arriver à prédire ou est-ce que la balle va atterir ! Cela semble compliqué au premier abord cependant vous verrez qu'avec quelques explications tout sera plus clair ;) Je vais vous montrer une technique mathématique permettant de prédire l'arrivée de la balle, cependant il en existe plusieurs et libre à vous de choisir une autre méthode que celle décrite ci-dessous.

## Partie 1

Comment peut-on prédire ou est-ce que la balle va atterrir ? Il existe plusieurs cas comme on peut le voir ci-dessous

![hint](/ressources/TP4/hint_1.png)

Comme on peut le voir la balle a un vecteur direction qui permet de savoir ou est-ce que la balle se dirige. Une des techniques qu’on peut employer pour prédire la balle est alors de « simuler » une autre balle qui aura les mêmes coordonnées que le vecteur de direction de la balle initiale mais aura un temps d’avance par rapport à ce vecteur. Un exemple graphique sera plus parlant.

![hint](/ressources/TP4/hint_2.png)

Les vecteurs de couleur rouge sont des vecteurs qui permettent de prédire la prochaine position de la balle. On peut voir que la balle n’a pas encore atterrit dans la deuxième figure cependant la raquette saura déjà ou se positionner en suivant la position du vecteur de coordonnées (dx1,dy1).
Pour construire ce vecteur on prend le vecteur direction initial, on le duplique et on l'agrandit jusqu’à ce que ce vecteur touche un mur, à partir de là on peut construire un deuxième vecteur qui aura pour coordonnées (dx’,-dy’) que j’appelle (dx1,dy1) dans la figure. On peut répéter cela jusqu’à ce qu’on atteigne la limite du « plateau » de jeu.

Si ça sonne compliqué pas de panique, on va y aller pas à pas, la première étape est de prédire les nouvelles coordonnées de la balle, pour ce faire on va créer une nouvelle classe NewCoordinates qui calculera la prochaine prédiction !

Pour ce faire vous avez une nouvelle classe NewCoordinates et BallDirection.

Afin de simplifier l'algorithme nous allons prédire au maximum que les deux prochains vecteurs

```py
class NewCoordinates:
    def __init__(self, x, y, x_v, y_v):
        # position X des nouveaux coordonnées de la balle
        self.x = x
        # position Y des nouveaux coordonnées de la balle
        self.y = y
        # Vélocité sur l'axe X
        self.x_v = x_v
        # Vélocité sur l'axe Y
        self.y_v = y_v

    # Fonction permettant de calculer les coordonnées X de prédiction
    def get_new_x(self):
        # à completer

    # Fonction permettant de calculer les coordonnées Y de prédiction
    def get_new_y(self):
        # à completer

    # Fonction permettant de calculer la longueur max du vecteur X
    def x_length(self):
        # à completer

    # Fonction permettant de calculer la longueur max du vecteur Y
    def y_length(self):
         # à completer

    # Fonction permettant de savoir si le vecteur prédit a toucher un mur
    def hit_top_or_bottom(self):
        # à completer
```

Une fois que vous aurez codé cette fonction vous pourrez lancer le code et voir le vecteur que vous aurez dessiné dans le jeu ! Oui pour vous aider j'ai dessiner le vecteur de la classe NewCoordinates, ainsi si la balle suit le chemin du vecteur c'est bon signe !

## Exemple de calcul correct de prédiction :

![hint](/ressources/TP4/hint_3.png)
![hint](/ressources/TP4/hint_4.png)

# PARTIE 2

Dans cette partie il faudra modifier la classe BallDirection en complétant cette fonction !

```py
    # Fonction permettant de prédire les nouveaux coordonées de la balle
    def predict_next_coordinate(self):
        ball= self.ball
        # Etape 1 On calcule les nouveaux coordonnées
            next_coordinates = ...
        # Etape 2 Si la balle a toucher un mur alors on doit recalculer le vecteur
        if next_coordinates.hit_top_or_bottom():
            # A completer
        else:
            # A completer
```

Une fois que cela sera fait il suffira à la raquette de suivre ces coordonnées et le tour est jouer, vous avez une IA qui prédit exactement ou la balle va atterir ! Vous pouvez ajouter des erreurs de prédiction pour avoir une IA encore plus intelligente et qui se rapproche plus d'un comportement humain (car oui l'humain fait toujours des erreurs !).

A vous de jouer !
