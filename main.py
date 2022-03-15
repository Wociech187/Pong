import pygame #Zaimportowanie biblioteki Pygame
import sys #Zaimportowanie biblioteki systemowej
import time #Zaimportowanie bilbioteki czasu
from object import pilka #Zaimportowanie klasy pilka z pliku object.py
from object import paletka #Zaimportowanie klasy paletka z pliku object.py


if __name__ == "__main__": #Jeśli program jest programem głównym
    class Game(object):
        def __init__(self): #Stworzenie fukcji inicjalizującej
            self.clock = pygame.time.Clock() #Utworzenie obiektu zegara
            icon = pygame.image.load("pong.png") #Zaimportowanie ikony okienka
            self.screen_image = pygame.image.load("nature-2384_960_720.jpg") #Zaimportowanie tła okna
            pygame.init() #Zainicjalizowanie biblioteki
            self.resolution = [700,600] #Utworzenie listy z rozdzielczością obrazu
            self.display = pygame.display.set_mode(self.resolution) #Utworznie obiektu ekranu
            pygame.display.set_caption("Taki tam Pong") #Nadanie tytułu dla okna
            pygame.display.set_icon(icon) #Ustawienie ikony
            self.dt = 0.0 #Utworzenie zmiennej delta time
            self.prev_time = time.time() #Pobranie czasu obecnego
            self.MAX_FPS = 144 #Ustawienie maksymalnej liczby FPS dla lepszej wydajności na komputerach o niższej mocy obliczeniowej

            #Zdefiniowanie pozycji początkowej dla obiektów piłki i graczy pos_x1 i pos_y1 dla gracza 1; pos_x2 i pos_y2 dla gracza 2 i ball_x oraz ball_y dla piłki
            self.pos_x1 = 10
            self.pos_y1 = self.resolution[1] / 2 - 90
            self.pos_x2 = self.resolution[0] - 25 - 10
            self.pos_y2 = self.resolution[1] / 2 - 90

            self.ball_x = self.resolution[0] / 2 - 10
            self.ball_y = self.resolution[1] / 2  - 10

            #Ustawienie prędkości poruszania się obiektów player_speed dla graczy i x_speed oraz y_speed dla piłki

            self.player_speed = 5
            self.x_speed = 1
            self.y_speed = 1

            #Utworzenie obiektów piłki i graczy oraz przekazanie im argumentu self, czyli klasa bala otrzyma dostęp do wszystkich zmiennych klasy Game tak samo dla klasy palatka. Obie klasy zamieszczone są w pliku object.py

            self.bala = pilka(self)
            self.players = paletka(self)

            self.paused = False #Ustawienie początkowego stany gry, Pauza gry ustawiona na Fałsz

            #Import czcionek do wyświetlenia na ekranie podczas końca gry
            self.font = pygame.font.SysFont(None,50)
            self.font2 = pygame.font.SysFont(None,30)

            while True: #Zapętlenie wykonywania programu
                    if self.paused == True: #Jeśli gra się zakończyła
                        for ev in pygame.event.get(): #Pętla która sprawdza czy system wykryje jakiś event z okna
                            if ev.type == pygame.QUIT: #Jeśli zostanie naciśnięty "zamnij okno" to zamyka gre
                                pygame.QUIT
                                sys.exit()
                            keys = pygame.key.get_pressed() #pobranie wszystkich dostępnych klawiszy
                            if keys[pygame.K_c]: #Jeśli klawisz c naciśnięty
                                game = Game() #Uruchomi grę ponownie
                            if keys[pygame.K_ESCAPE]: #Jeśli klawisz ESC naciśnięty zamyka grę i okno
                                pygame.QUIT
                                sys.exit()

                        self.msg(f"{self.bala.win} win the game", (132,45,21)) #Wyświetlenie wiadomości w kolorze, kto wygrał gre
                        self.msg2("Press ESC to QUIT or c to continue the game", (132,45,21)) #Wyświetlenie wiadomości co użytkownik może zrobić dalej
                        pygame.display.flip() #Odświerzenie ekranu
                    if self.paused == False: #Jeśli gra trwa
                        self.clock.tick(100) #Ustawienie ilości FPS komputera na 100
                        self.now = time.time() #Pobranie aktualnego czasu
                        self.dt = self.prev_time - self.now #Zmiana wartości delta time. Delta time to różnica czasu początku jednej klatki do początku drugiej klatki
                        self.prev_time = self.now #Teraz początkiem klatki będzie now i tak do końca trwania gry
                        #Delta time pomaga zapobiec opóźnieniom w przypadku komputerów o niższej mocy obliczeniowej. Np. Komputer o wydajności 60 FPS będzie miał taką samą prędkość jak komputer z 30FPS. Kosztem jest czas im więcej FPS tym czas krótszy.
                        #Gdyby delta time nie zostało zaimplemetowanie a gra miałaby być onnline to gracze o niższej mocy obliczeniowej komputera nie mogli by wygrać rozgrywki


                        #Zmiana prędkości obiektu piłki z uwgdlędnieniem maksymalnej liczby FPS oraz wcześniej wspomnianego delta time
                        self.y_speed += self.y_speed * self.dt * self.MAX_FPS
                        self.x_speed += self.x_speed * self.dt * self.MAX_FPS

                        for ev in pygame.event.get(): #Pętla która pobiera eventy z biblioteki
                            if ev.type == pygame.QUIT: #Jeśli naciśnięto "zamknij okno" to gra się zamyka
                                pygame.QUIT
                                sys.exit()
                        self.move() #Wykonanie fukcji poruszania obiektami. Funkcja napisana niżej

                        self.display.blit(self.screen_image, (0, 0)) #Narysowanie ekranu
                        self.draw() #Wykonanie funkcji rysowania obiektów. Funkcja napisana niżej
        def draw(self): #Funckja ogólna do rysowania
            self.bala.draw() #wykonanie funckji rysowania obiektu piłki. Funckja znajduje się w klasie pilka w pliku object.py
            self.players.draw() #wykonanie funkcji rysowania obiektu graczy. Funkcja znajduje się w klasie paletka w pliku object.py
            pygame.display.flip() #Odświerzenie ekranu
        def move(self): #Funckja poruszania
            self.bala.move() #wykonanie funckji poruszania obiektu piłki. Funckja znajduje się w klasie pilka w pliku object.py
            self.players.move()#wykonanie funkcji poruszania obiektu graczy. Funkcja znajduje się w klasie paletka w pliku object.py
        def msg(self,msgs,color): #Funcja odpowiadająca za wiadomośc kto wygrał
            self.screen_text = self.font.render(msgs, True,color) #Pobiera wiadomość do zmiennej
            self.display.blit(self.screen_text, [self.resolution[0] / 2 - 160, self.resolution[1] / 2 - 10]) #Wyświetla na ekranie text - pierwszy argument w określonym miejscu ekranu - drugi argument
        def msg2(self,msgs,color): #Funcja odpowiadająca za wiadomośc o dalszych możliwościach programy
            self.screen_text = self.font2.render(msgs, True,color) #Pobiera wiadomość do zmiennej
            self.display.blit(self.screen_text, [self.resolution[0] / 2 - 200, self.resolution[1] / 2 + 100])  #Wyświetla na ekranie text - pierwszy argument w określonym miejscu ekranu - drugi argument

game = Game() #Utworzenie obiektu dla klasy Game
