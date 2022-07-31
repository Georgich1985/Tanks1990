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
        self.image = texture  # pygame.Surface(size)
        # self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self, texture, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        if flag1 == True:
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
        if flag1 == True:
            if self.direction == 1:
                self.rect.x += self.speed
            elif self.direction == 2:
                self.rect.x -= self.speed
            elif self.direction == 3:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed


def options():
    global opt_proc
    opt_proc = True
    button_list = pygame.sprite.Group()
    back_button = Button((50, 50), back_button_img)
    volume_button = Button((WIDTH / 2, 50), volume_button_img)
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
                    current_volume += 0.01
                    pygame.mixer.music.set_volume(current_volume)
                if minus_button.rect.collidepoint(mouse_pos):
                    current_volume -= 0.01
                    pygame.mixer.music.set_volume(current_volume)
                if right_button.rect.collidepoint(mouse_pos):
                    flag = False
                if left_button.rect.collidepoint(mouse_pos):
                    flag = True
        pygame.display.flip()


def start_game():
    global flag1, opt_proc, game_proc, menu_proc, button_moving_speed
    fps = 30
    pygame.mixer.music.load(battle1_music)
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
    pygame_clock = pygame.time.Clock()
    player = Player()
    vrag1 = Enemy(vrag1_img, (300, 300))
    continue_button_pause = Button((WIDTH - 155, 35), continue_button_img)
    options_button_pause = Button((WIDTH - options_button_img.get_width() // 2 - 7, continue_button_pause.rect.centery + options_button_img.get_height() + 7), options_button_img)
    menu_button_pause = Button((WIDTH - menu_button_img.get_width() // 2 - 7, options_button_pause.rect.centery + menu_button_img.get_height() + 7), menu_button_img)
    quit_button_pause = Button((WIDTH - quit_button_img.get_width() // 2 - 7, menu_button_pause.rect.centery + quit_button_img.get_height() + 7), quit_button_img)
    # quit_button_pause = Button((WIDTH + 100, menu_button_pause.rect.centery + quit_button_img.get_height() + 7), quit_button_img)
    missiles_list = pygame.sprite.Group()
    object_list = pygame.sprite.Group()
    object_list.add(player, vrag1)
    while game_proc:
        pygame_clock.tick(fps)
        screen.blit(fon1_img, fon1_img.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flag1 == True:
                    missile = Missile(missile_img, player.getPos(), player.getDirection(), 5)
                    object_list.add(missile)
                    missiles_list.add(missile)
                if event.key == pygame.K_ESCAPE:
                    flag1 = False
                    object_list.add(continue_button_pause, options_button_pause, menu_button_pause, quit_button_pause)
                    # while True:
                    #     pygame.time.wait(1000)
                    #     quit_button_pause.rect.x -= 1
                    #     if quit_button_pause.rect.centerx == WIDTH - quit_button_img.get_width() // 2 - 7:
                    #         break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_button_pause.rect.collidepoint(mouse_pos):
                    flag1 = True
                    object_list.remove(continue_button_pause, options_button_pause, menu_button_pause, quit_button_pause)
                if options_button_pause.rect.collidepoint(mouse_pos):
                    options()
                if menu_button_pause.rect.collidepoint(mouse_pos):
                    menu("pause")
                if quit_button_pause.rect.collidepoint(mouse_pos):
                    menu_proc = False
                    game_proc = False
        object_list.update()
        object_list.draw(screen)
        pygame.display.flip()


def menu(main_or_pause):
    global menu_proc, game_proc, flag1
    menu_proc = True
    button_list = pygame.sprite.Group()
    play_button = Button((WIDTH / 2, HEIGHT / 2 - 100), play_button_img)
    options_button = Button((WIDTH / 2, HEIGHT / 2), options_button_img)
    quit_button = Button((WIDTH / 2, HEIGHT / 2 + 100), quit_button_img)
    newgame_button = Button((WIDTH / 2, HEIGHT / 2 - 100), newgame_button_img)
    back_button = Button((50, 50), back_button_img)
    button_list.add(options_button, quit_button)
    if main_or_pause == "main":
        button_list.add(play_button)
    elif main_or_pause == "pause":
        button_list.add(newgame_button, back_button)
    # pygame.mixer.music.play()
    while menu_proc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if quit_button.rect.collidepoint(mouse_pos):
                    menu_proc = False
                    game_proc = False
                if options_button.rect.collidepoint(mouse_pos):
                    options()
                if main_or_pause == "main":
                    if play_button.rect.collidepoint(mouse_pos):
                        start_game()
                if main_or_pause == "pause":
                    if newgame_button.rect.collidepoint(mouse_pos):
                        flag1 = True
                        start_game()
                    if back_button.rect.collidepoint(mouse_pos):
                        menu_proc = False
        screen.blit(fon1_img, fon1_img.get_rect())
        button_list.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    menu("main")
