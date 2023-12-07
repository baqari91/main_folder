import pygame
import sys

pygame.init()

info = pygame.display.Info()

width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini App")

#RGB RED GREEN BLUE
red = (255, 100, 100)
green = (100, 255, 100)


player_image = pygame.image.load("bee.png")


class Player:
    def __init__(self, speed, size, health, image):
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = pygame.Rect(width/2, height/2, self.size, self.size)
        self.rect.center = [width/2, height/2]
        self.speed = speed
        self.cur_speed_w = 0
        self.cur_speed_h = 0
        self.health = health


    def draw_player(self):
        # pygame.draw.rect(screen, green, self.rect)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_player(self):
        self.rect.x += self.cur_speed_w
        self.rect.y += self.cur_speed_h

        #საზღვრის დაწესება
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height

    def update(self):
        self.draw_player()
        self.move_player()

player = Player(1, 60, 100, player_image)


run = True
while run:
    screen.fill(red)
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.cur_speed_w = -player.speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.cur_speed_w = player.speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.cur_speed_h = -player.speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.cur_speed_h = player.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                player.cur_speed_w = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                player.cur_speed_h = 0

    pygame.display.update()


pygame.quit()
sys.exit()