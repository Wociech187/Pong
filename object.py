import pygame
class paletka():
    def __init__(self,game):
        self.game = game
        self.display = self.game.display
        self.pos1_x = self.game.pos_x1
        self.pos1_y = self.game.pos_y1
        self.pos2_x = self.game.pos_x2
        self.pos2_y = self.game.pos_y2
        self.player1 = pygame.Rect(self.pos1_x,self.pos1_y,25,150)
        self.player2 = pygame.Rect(self.pos2_x, self.pos2_y, 25, 150)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player1.y -= self.game.player_speed
        if keys[pygame.K_DOWN]:
            self.player1.y += self.game.player_speed
        if keys[pygame.K_w]:
            self.player2.y -= self.game.player_speed
        if keys[pygame.K_s]:
            self.player2.y += self.game.player_speed
        if self.player1.top <= 0:
            self.player1.y += 10
        if self.player1.bottom >= self.game.resolution[1]:
            self.player1.y -= 10
        if self.player2.top <= 0:
            self.player2.y += 10
        if self.player2.bottom >= self.game.resolution[1]:
            self.player2.y -= 10


    def draw(self):
        pygame.draw.rect(self.display, (0, 150, 255), self.player1)
        pygame.draw.rect(self.display, (0, 150, 255), self.player2)
class pilka():
    def __init__(self,game):
        self.game = game
        self.display = self.game.display
        self.pos_x = self.game.ball_x
        self.pos_y = self.game.ball_y
        self.ball = pygame.Rect(self.pos_x,self.pos_y,30,30)
        self.speed_x = self.game.x_speed
        self.speed_y = self.game.y_speed

    def move(self):
        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y

        if self.ball.colliderect(self.game.players.player1):
            if abs(self.ball.left - self.game.players.player1.right) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.right - self.game.players.player1.left) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.bottom - self.game.players.player1.top) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
            if abs(self.ball.top - self.game.players.player1.bottom) > 10:
                self.speed_y *= -1
                self.speed_x *= -1
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


        if self.ball.top <= 0 or self.ball.bottom >= self.game.resolution[1]:
            self.speed_y *= -1
        if self.ball.left <= 0:
            self.win = "Player2"
            self.game.paused = True
        if self.ball.right >= self.game.resolution[0]:
            self.win = "Player1"
            self.game.paused = True
    def draw(self):
        pygame.draw.ellipse(self.display, (125,50,75), self.ball)

