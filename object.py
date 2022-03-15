import pygame
class paletka(): #Utworznie klasy dla graczy
    def __init__(self,game): #Zainicjalizowanie klasy oraz wymagany argument game czyli cała klasa Game
        self.game = game #Przypisanie do klasy wszyskich zmiennych klasy Game do zmiennej game

        #Pobieranie informacji z klasy Game o ekranie
        self.display = self.game.display
        self.pos1_x = self.game.pos_x1
        self.pos1_y = self.game.pos_y1
        self.pos2_x = self.game.pos_x2
        self.pos2_y = self.game.pos_y2

        #Utworznie obiektu prostokąta dla obu graczy
        self.player1 = pygame.Rect(self.pos1_x,self.pos1_y,25,150)
        self.player2 = pygame.Rect(self.pos2_x, self.pos2_y, 25, 150)

    def move(self): #Funkcja poruszania
        keys = pygame.key.get_pressed() #Pobranie wszystkich klawiszy
        if keys[pygame.K_UP]: #Jeśli klawisz w górę wciśnięty
            self.player1.y -= self.game.player_speed #Odejmij od pozycji gracza1 prędkość gracza
        if keys[pygame.K_DOWN]: #Jeśli klawisz w dół wciśnięty
            self.player1.y += self.game.player_speed #Dodaj do pozycji gracza1 prędkość gracza
        if keys[pygame.K_w]:  #Jeśli klawisz w  wciśnięty
            self.player2.y -= self.game.player_speed  #Odejmij od pozycji gracza2 prędkość gracza
        if keys[pygame.K_s]:  #Jeśli klawisz s wciśnięty
            self.player2.y += self.game.player_speed  #Dodaj do pozycji gracza2 prędkość gracza

        #Kolizje paletek
        if self.player1.top <= 0: #Jeśli góra gracza nr.1 jest mniejsza lub równa 0 - góra ekranu
            self.player1.y += 10 #Zmiena pozycje gracza1 żeby nie mógł dalej poruszać się w górę
        if self.player1.bottom >= self.game.resolution[1]: #Jeśli dół gracza nr.1 jest większy lub równy maksymalnej rozdzielczości
            self.player1.y -= 10  #Zmiena pozycje gracza1 żeby nie mógł dalej poruszać się w dół

        if self.player2.top <= 0: #Jeśli góra gracza nr.2 jest mniejsza lub równa 0 - góra ekranu
            self.player2.y += 10 #Zmiena pozycje gracza2 żeby nie mógł dalej poruszać się w górę
        if self.player2.bottom >= self.game.resolution[1]:  #Jeśli dół gracza nr.2 jest większy lub równy maksymalnej rozdzielczości
            self.player2.y -= 10  #Zmiena pozycje gracza2 żeby nie mógł dalej poruszać się w dół


    def draw(self): #Rysowanie na ekranie graczy
        pygame.draw.rect(self.display, (0, 150, 255), self.player1) #Narysowanie obiektu gracza nr.1
        pygame.draw.rect(self.display, (0, 150, 255), self.player2) #Narywanie obiektu gracza nr.2

class pilka(): #Utworzenie klasy piłki
    #Funcja __init__ działa na takiej samej zasadzie jak funckja __init__ klasy paletka
    def __init__(self,game):
        self.game = game
        self.display = self.game.display
        self.pos_x = self.game.ball_x
        self.pos_y = self.game.ball_y
        self.ball = pygame.Rect(self.pos_x,self.pos_y,30,30)
        self.speed_x = self.game.x_speed
        self.speed_y = self.game.y_speed

    def move(self): #Funkcja poruszania piłki
        #Domyślnie ustanione że piłka będzie poruszać się w lewą górną cześć ekranu
        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y

        #Kolizje piłki z graczem nr.1
        if self.ball.colliderect(self.game.players.player1): #Funckja colliderect sprawdza czy obiekt ma kolizję z obiektem gracza nr.1. Jeśli tak to:
            if abs(self.ball.left - self.game.players.player1.right) > 10: #Jeśli różnica odległości między lewą częścią piłki a prawą częścią gracza nr.1 jest większa od 10.
                #Liczba 10 jest domyślnym standardem przyjmowanych różnicy odlegości w takich typu grach

                #Po wykryciu tego typu zderzenia zmienia kierunek ruchu piłki
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.right - self.game.players.player1.left) > 10:  #Jeśli różnica odległości między prawą częścią piłki a lewą częścią gracza nr.1 jest większa od 10
                # Po wykryciu tego typu zderzenia zmienia kierunek ruchu piłki
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.bottom - self.game.players.player1.top) > 10:  #Jeśli różnica odległości między dolną częścią piłki a górną częścią gracza nr.1 jest większa od 10
                # Po wykryciu tego typu zderzenia zmienia kierunek ruchu piłki
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.top - self.game.players.player1.bottom) > 10: #Jeśli różnica odległości między górną częścią piłki a dolną częścią gracza nr.1 jest większa od 10
                # Po wykryciu tego typu zderzenia zmienia kierunek ruchu piłki
                self.speed_y *= -1
                self.speed_x *= -1

        #Kolizje piłki z graczem nr.2 działają na tej samej zasadzie co kolizje piłki z graczem nr. 1 jak powyżej
        if self.ball.colliderect(self.game.players.player2):
            if abs(self.ball.left - self.game.players.player2.right) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.right - self.game.players.player2.left) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.bottom - self.game.players.player2.top) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.top - self.game.players.player2.bottom) > 10:
                self.speed_y *= -1
                self.speed_x *= -1

        #Kolizje piłki z ekranem
        if self.ball.top <= 0 or self.ball.bottom >= self.game.resolution[1]: #Jeśli góra lub dół piłki dotykają dolnej lub górnej części ekranu
            self.speed_y *= -1 #Pomnóż prędkość y piłki o -1 co zmienia kierunek ruchu piłki
        if self.ball.left <= 0: #Jeśli lewa część piłki dotyka lewej krawędzi ekranu
            self.win = "Player2" #Przekaż że wygrał gracz nr.2
            self.game.paused = True #Ustaw że gra jest przerwana. Główny plik z grą
        if self.ball.right >= self.game.resolution[0]: #Jeśli prawa część piłki dotyka prawej krawędzi ekrany
            self.win = "Player1" #Przekaż że wygrał gracz nr.1
            self.game.paused = True #Przerwij gre jak wyżej wspomniane
    def draw(self): #Rysowanie piłki
        pygame.draw.ellipse(self.display, (125,50,75), self.ball) #Wywołanie funkcji pygame.draw.ellipse która narysuje okrągłą piłkę

