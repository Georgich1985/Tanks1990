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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, texture, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.lastFire = 0
        self.directionInt = 4
        self.direction = "right"
        self.directionListUp = ["down", "right", "left"]
        self.directionListDown = ["up", "right", "left"]
        self.directionListRight = ["up", "down", "left"]
        self.directionListLeft = ["up", "down", "right"]

    def getPos(self):
        return self.rect.center

    def getDirection(self):
        return self.direction

    def canFire(self):
        if time.time() - self.lastFire >= 3:
            self.lastFire = time.time()
            return True
        return False

    def update(self):
        if self.direction == "up":
            self.rect.y -= 5
            self.image = vrag1_img
            self.directionInt = 4
        elif self.direction == "down":
            self.rect.y += 5
            self.image = pygame.transform.rotate(vrag1_img, 180)
            self.directionInt = 3
        elif self.direction == "right":
            self.rect.x += 5
            self.image = pygame.transform.rotate(vrag1_img, -90)
            self.directionInt = 1
        elif self.direction == "left":
            self.rect.x -= 5
            self.image = pygame.transform.rotate(vrag1_img, 90)
            self.directionInt = 2
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
            self.direction = self.directionListRight[random.randint(0, 2)]
        elif self.rect.left <= 0:
            self.rect.left = 1
            self.direction = self.directionListLeft[random.randint(0, 2)]
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - 1
            self.direction = self.directionListDown[random.randint(0, 2)]
        elif self.rect.top <= 0:
            self.rect.top = 1
            self.direction = self.directionListUp[random.randint(0, 2)]


class Missile(pygame.sprite.Sprite):
    def __init__(self, texture, pos, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = direction
        self.speed = speed
        self.owner = "player"

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed


def pause():
    global screenshot
    continue_button_pause = Button((WIDTH/2, HEIGHT/2 +50), continue_button_img)
    options_button_pause = Button((WIDTH/2,
                                   continue_button_pause.rect.centery + options_button_img.get_height() + 7),
                                  options_button_img)
    menu_button_pause = Button((WIDTH/2,
                                options_button_pause.rect.centery + menu_button_img.get_height() + 7), menu_button_img)
    quit_button_pause = Button((WIDTH/2,
                                menu_button_pause.rect.centery + quit_button_img.get_height() + 7), quit_button_img)
    button_list = pygame.sprite.Group()
    button_list.add(continue_button_pause, options_button_pause, menu_button_pause, quit_button_pause)
    button_list.draw(screen)
    pause_proc = True
    while pause_proc:
        screen.blit(fon1_img, fon1_img.get_rect())
        button_list.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_button_pause.rect.collidepoint(mouse_pos):
                    return True
                if options_button_pause.rect.collidepoint(mouse_pos):
                    options()
                if menu_button_pause.rect.collidepoint(mouse_pos):
                    return False
                if quit_button_pause.rect.collidepoint(mouse_pos):
                    sys.exit()
        pygame.display.flip()


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
        global current_volume
        if resources.flag == True:
            button_list.remove(arrows_button)
            button_list.add(wasd_button)
            button_list.draw(screen)
        elif resources.flag == False:
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
                    resources.flag = False
                if left_button.rect.collidepoint(mouse_pos):
                    resources.flag = True
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
    enemy_list = []
    enemy_list.append(vrag1)
    missiles_list = pygame.sprite.Group()
    object_list = pygame.sprite.Group()
    object_list.add(player, vrag1)
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
                if event.key == pygame.K_ESCAPE:
                    pygame.image.save(screen, "screenshot.jpg")
                    game_proc = pause()
        for enemy in enemy_list:
            if enemy.canFire():
                missile = Missile(missile_img, enemy.getPos(), enemy.getDirection(), 7)
                missiles_list.add(missile)
                object_list.add(missile)
        object_list.update()
        object_list.draw(screen)
        pygame.display.flip()


def menu():
    pygame.mixer.music.load(fon_music)
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
    menu_proc = True
    button_list = pygame.sprite.Group()
    play_button = Button((WIDTH / 2, HEIGHT / 2 + 40), newgame_button_img)
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
