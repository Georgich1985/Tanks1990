import pygame
import os

HEIGHT = 600
WIDTH = 600

current_volume = 0.05
flag = True
flag1 = True
menu_proc = True
opt_proc = True
game_proc = True

main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "image")
sound_folder = os.path.join(main_folder, "sound")

beton_img = pygame.image.load(os.path.join(image_folder, 'landscape/beton.png'))
brick_img = pygame.image.load(os.path.join(image_folder, 'landscape/brick.png'))
forest_img = pygame.image.load(os.path.join(image_folder, 'landscape/forest.png'))
pol_img = pygame.image.load(os.path.join(image_folder, 'landscape/pol.png'))
water_img = pygame.image.load(os.path.join(image_folder, 'landscape/water.png'))

fon1_img = pygame.image.load(os.path.join(image_folder, 'background1.jpg'))
fon2_img = pygame.image.load(os.path.join(image_folder, 'background2.jpg'))

playerV1_img = pygame.image.load(os.path.join(image_folder, 'player/tankv1.png'))
playerV2_img = pygame.image.load(os.path.join(image_folder, 'player/tankv2.png'))
playerV3_img = pygame.image.load(os.path.join(image_folder, 'player/tankv3.png'))
playerV4_img = pygame.image.load(os.path.join(image_folder, 'player/tankv4.png'))

play_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/play_button.png'))
options_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/options_button.png'))
quit_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/quit_button.png'))
volume_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/volume_button.png'))
plus_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/plus_button.png'))
minus_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/minus_button.png'))
back_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/back_button.png'))
left_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/left_button.png'))
right_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/right_button.png'))
fire_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/fire_button.png'))
wasd_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/wasd_button.png'))
arrows_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/arrows_button.png'))
continue_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/continue_button.png'))
newgame_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/newgame_button.png'))
menu_button_img = pygame.image.load(os.path.join(image_folder, 'buttons/menu_button.png'))

vrag1_img = pygame.image.load(os.path.join(image_folder, 'enemies/vrag1.png'))
vrag2_img = pygame.image.load(os.path.join(image_folder, 'enemies/vrag2.png'))
vrag3_img = pygame.image.load(os.path.join(image_folder, 'enemies/vrag3.png'))

missile_img = pygame.image.load(os.path.join(image_folder, 'missile.png'))

fon_music = os.path.join(sound_folder, 'Main_Theme.mp3')
battle1_music = os.path.join(sound_folder, 'Battle1.mp3')
