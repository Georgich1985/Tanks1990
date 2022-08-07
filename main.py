from player import *
import time
import random
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, texture):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Base(pygame.sprite.Sprite):
    def __init__(self, texture, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self, texture, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x += 5


class Missile(pygame.sprite.Sprite):
    def __init__(self, texture, pos, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = direction
        self.speed = speed

    def update(self):
        if self.direction == 1:
            self.rect.x += self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed


def options():
    opt_proc = True
    button_list = pygame.sprite.Group()
    back_button = Button((50, HEIGHT / 2 + 80), back_button_img)
    volume_button = Button((WIDTH / 2, HEIGHT / 2 + 80), volume_button_img)
    plus_button = Button((volume_button.rect.centerx - volume_button_img.get_width() // 2 -
                          plus_button_img.get_width() // 2, volume_button.rect.centery), plus_button_img)
    minus_button = Button((volume_button.rect.centerx + volume_button_img.get_width() // 2 +
                           minus_button_img.get_width() // 2, volume_button.rect.centery), minus_button_img)
    left_button = Button((plus_button.rect.centerx, volume_button.rect.centery + 100), left_button_img)
    right_button = Button((minus_button.rect.centerx, volume_button.rect.centery + 100), right_button_img)
    wasd_button = Button((volume_button.rect.centerx, volume_button.rect.centery + 100), wasd_button_img)
    arrows_button = Button((volume_button.rect.centerx, volume_button.rect.centery + 100), arrows_button_img)
    button_list.add(back_button, volume_button, plus_button, minus_button, left_button, right_button)
    screen.blit(fon1_img, fon1_img.get_rect())
    button_list.draw(screen)
    while opt_proc:
        global current_volume, flag
        if flag == True:
            button_list.remove(arrows_button)
            button_list.add(wasd_button)
            button_list.draw(screen)
        elif flag == False:
            button_list.remove(wasd_button)
            button_list.add(arrows_button)
            button_list.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.rect.collidepoint(mouse_pos):
                    opt_proc = False
                if plus_button.rect.collidepoint(mouse_pos):
                    current_volume += 0.05
                    pygame.mixer.music.set_volume(current_volume)
                if minus_button.rect.collidepoint(mouse_pos):
                    current_volume -= 0.05
                    pygame.mixer.music.set_volume(current_volume)
                if right_button.rect.collidepoint(mouse_pos):
                    flag = False
                if left_button.rect.collidepoint(mouse_pos):
                    flag = True
        pygame.display.flip()


def start_game():
    pygame.mixer.music.load(battle1_music)
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
    game_proc = True
    fps = 30
    pygame_clock = pygame.time.Clock()
    player = Player()
    vrag1 = Enemy(vrag1_img, (300, 300))
    base = Base(base_img, (300, 500))
    missiles_list = pygame.sprite.Group()
    object_list = pygame.sprite.Group()
    object_list.add(player, vrag1, base)
    while game_proc:
        pygame_clock.tick(fps)
        screen.blit(fon2_img, fon2_img.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    missile = Missile(missile_img, player.getPos(), player.getDirection(), 7)
                    object_list.add(missile)
                    missiles_list.add(missile)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
        # for m in missiles_list:

        object_list.update()
        object_list.draw(screen)
        pygame.display.flip()


def menu():
    pygame.mixer.music.load(fon_music)
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
    menu_proc = True
    button_list = pygame.sprite.Group()
    play_button = Button((WIDTH / 2, HEIGHT / 2 + 40), play_button_img)
    options_button = Button((WIDTH / 2, HEIGHT / 2 + 120), options_button_img)
    quit_button = Button((WIDTH / 2, HEIGHT / 2 + 200), quit_button_img)
    button_list.add(play_button, options_button, quit_button)
    while menu_proc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if quit_button.rect.collidepoint(mouse_pos):
                    menu_proc = False
                if options_button.rect.collidepoint(mouse_pos):
                    options()
                if play_button.rect.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    start_game()
        screen.blit(fon1_img, fon1_img.get_rect())
        button_list.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    menu()
