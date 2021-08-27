WIDTH, HEIGHT = 900, 500
PADDLE_OFFSET = 20


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
        return self.x + (self.x_v * min(self.x_length(), self.y_length()))

    # Fonction permettant de calculer les coordonnées Y de prédiction
    def get_new_y(self):
        return self.y + (self.y_v * min(self.x_length(), self.y_length()))

    # Fonction permettant de calculer la longueur max du vecteur X
    def x_length(self):
        if(self.x_v > 0):
            return (WIDTH - PADDLE_OFFSET - self.x)/self.x_v
        else:
            return (self.x - PADDLE_OFFSET)/-self.x_v

    # Fonction permettant de calculer la longueur max du vecteur Y
    def y_length(self):
        if(self.y_v > 0):
            return (HEIGHT - self.y)/self.y_v
        else:
            return (self.y)/-self.y_v

    # Fonction permettant de savoir si le vecteur prédit a toucher un mur
    def hit_top_or_bottom(self):
        return self.x_length() > self.y_length()
