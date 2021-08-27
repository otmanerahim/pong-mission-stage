from NewCoordinates import NewCoordinates
import pygame


class BallDirection:
    def __init__(self, screen,ball):
        self.screen = screen
        # Le point de prédiction final 
        self.final_y = 0
        # Les prochaines coordonnées de la balle 
        self.next_coordinates= NewCoordinates(0,0,0,0)
        # les coordonées final de la balle 
        self.final_coordinates = NewCoordinates(0,0,0,0)
        self.ball=ball
    

    # Fonction permettant de prédire les nouveaux coordonées de la balle
    def predict_next_coordinate(self):
        ball= self.ball

        # On calcule les nouveaux coordonnées
        self.next_coordinates = NewCoordinates(
            ball.x_middle(), ball.y_middle(), ball.get_dx(), ball.get_dy())
        next_coordinates = self.next_coordinates
        
        # Si la balle a toucher un mur alors on doit recalculer le vecteur
        if next_coordinates.hit_top_or_bottom():
            self.final_coordinates = NewCoordinates(next_coordinates.get_new_x(
            ), next_coordinates.get_new_y(), ball.get_dx(), -ball.get_dy())
            self.final_y = self.final_coordinates.get_new_y()
        else:
            self.final_y = next_coordinates.get_new_y()
        

    # Fonction permettant de dessiner le vecteur prédit
    def draw(self):
        ball= self.ball
        next_coordinates = self.next_coordinates
        final_coordinates = self.final_coordinates
        x_middle = ball.x_middle()
        y_middle = ball.y_middle()
        if next_coordinates.hit_top_or_bottom():
            pygame.draw.line(self.screen, (255, 0, 0), (ball.x_middle(),
                         ball.y_middle()), (next_coordinates.get_new_x(), next_coordinates.get_new_y()), 1)
        
            pygame.draw.line(self.screen, (255, 0, 0), (next_coordinates.get_new_x(
            ), next_coordinates.get_new_y()), (final_coordinates.get_new_x(), final_coordinates.get_new_y()), 1)
        else:
            pygame.draw.line(self.screen, (255, 0, 0), (ball.x_middle(),
                                                        ball.y_middle()), (next_coordinates.get_new_x(), next_coordinates.get_new_y()), 1)

    def get_ball_prediction_y(self):
        return self.final_y
