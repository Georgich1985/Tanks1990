import resources
from resources import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerV1_img
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2, HEIGHT - 50))
        self.direction = "top"

    def getPos(self):
        return self.rect.center

    def getDirection(self):
        return self.direction

    def update(self):
        pressed_button = pygame.key.get_pressed()
        if resources.flag == True:
            if pressed_button[pygame.K_w]:
                self.image = playerV1_img
                self.direction = "top"
                self.rect.y -= 5
                if self.rect.bottom <= 0:
                    self.rect.top = HEIGHT
            elif pressed_button[pygame.K_s]:
                self.image = pygame.transform.rotate(playerV1_img, 180)
                self.direction = "down"
                self.rect.y += 5
                if self.rect.top >= HEIGHT:
                    self.rect.bottom = 0
            elif pressed_button[pygame.K_a]:
                self.image = pygame.transform.rotate(playerV1_img, 90)
                self.direction = "left"
                self.rect.x -= 5
                if self.rect.right <= 0:
                    self.rect.left = WIDTH
            elif pressed_button[pygame.K_d]:
                self.image = pygame.transform.rotate(playerV1_img, -90)
                self.direction = "right"
                self.rect.x += 5
                if self.rect.left >= WIDTH:
                    self.rect.right = 0
        else:
            if pressed_button[pygame.K_UP]:
                self.rect.y -= 5
                if self.rect.bottom <= 0:
                    self.rect.top = HEIGHT
            if pressed_button[pygame.K_DOWN]:
                self.rect.y += 5
                if self.rect.top >= HEIGHT:
                    self.rect.bottom = 0
            if pressed_button[pygame.K_LEFT]:
                self.rect.x -= 5
                if self.rect.right <= 0:
                    self.rect.left = WIDTH
            if pressed_button[pygame.K_RIGHT]:
                self.rect.x += 5
                if self.rect.left >= WIDTH:
                    self.rect.right = 0
