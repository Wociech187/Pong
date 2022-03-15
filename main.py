import pygame
import sys
import time
from object import pilka
from object import paletka


if __name__ == "__main__":
    class Game(object):
        def __init__(self):
            self.clock = pygame.time.Clock()
            icon = pygame.image.load("pong.png")
            self.screen_image = pygame.image.load("nature-2384_960_720.jpg")
            pygame.init()
            self.resolution = [700,600]
            self.display = pygame.display.set_mode(self.resolution)
            pygame.display.set_caption("Taki tam Pong")
            pygame.display.set_icon(icon)
            self.dt = 0.0
            self.prev_time = time.time()
            self.MAX_FPS = 144

            self.pos_x1 = 10
            self.pos_y1 = self.resolution[1] / 2 - 90
            self.pos_x2 = self.resolution[0] - 25 - 10
            self.pos_y2 = self.resolution[1] / 2 - 90

            self.ball_x = self.resolution[0] / 2 - 10
            self.ball_y = self.resolution[1] / 2  - 10

            self.player_speed = 5
            self.x_speed = 1
            self.y_speed = 1

            self.bala = pilka(self)
            self.players = paletka(self)

            self.paused = False
            self.font = pygame.font.SysFont(None,50)
            while True:
                    if self.paused == True:
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                sys.exit()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_f]:
                                game = Game()
                        self.msg(f"{self.bala.win} win the game", (132,45,21))
                        pygame.display.flip()
                    if self.paused == False:
                        self.clock.tick(100)
                        self.now = time.time()
                        self.dt = self.prev_time - self.now
                        self.prev_time = self.now
                        print(self.dt)
                        self.y_speed += self.y_speed * self.dt * self.MAX_FPS
                        self.x_speed += self.x_speed * self.dt * self.MAX_FPS
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                sys.exit()
                        self.move()

                        self.display.blit(self.screen_image, (0, 0))
                        self.draw()
        def draw(self):
            self.bala.draw()
            self.players.draw()
            pygame.display.flip()
        def move(self):
            self.bala.move()
            self.players.move()
        def msg(self,msgs,color):
            self.screen_text = self.font.render(msgs, True,color)
            self.display.blit(self.screen_text, [self.resolution[0] / 2 - 160, self.resolution[1] / 2 - 10])

game = Game()
