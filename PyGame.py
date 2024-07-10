
import pygame 
import sys 
import random 
 
pygame.init() 
 
#COLORS 
black = (0, 0, 0) 
white = (255, 255, 255) 
blue = (0, 0, 255) 
 
 
# DISPLAY 
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height)) 
 
# BACKGROUND 
background_img = pygame.image.load("FlappyBackround.png") 
background_surf = pygame.transform.scale(background_img, (screen_width + 80, screen_height + 80)) 
background_rect = background_surf.get_rect(topleft=(0, 0)) 
 
# INSTRUCTIONS 
instructions_txt = "Instructions/press space to continue" 
instructions_font = pygame.font.Font(None, 30) 
instructions_render = instructions_font.render(instructions_txt, True, blue) 
instructions_rect = instructions_render.get_rect(center=(screen_width // 2, screen_height // 2)) 
 
# GAME END MESSAGE
lost_txt = "OH NO YOUR CRASHED"
option_txt = "Press ESC to end game or R to resart" 
Lost_font = pygame.font.SysFont("monospace", 50)
options_font = pygame.font.SysFont("monospace", 10)
red = (255,0,0)

# BIRD 
Bird_surface = pygame.image.load('bird.png').convert_alpha() 
Bird_surface = pygame.transform.scale(Bird_surface, (60, 60)) 
Bird_surface_rect = Bird_surface.get_rect(center=(screen_width / 2, screen_height / 2)) 
 
#PIPES 
#pipe_surface = pygame.image.load("Pipe1.png").convert_alpha() 
#pipe_surface = pygame.transform.scale(pipe_surface, (500,500)) 
#pipe_rect = pipe_surface.get_rect(bottom=screen_height, centerx=(screen_width/2)) 
pause = False
running = True 
while running: 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                running = False 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]: 
        Bird_surface_rect.y = Bird_surface_rect.y - 10 
    if keys[pygame.K_DOWN]: 
        Bird_surface_rect.y = Bird_surface_rect.y + 10 
    if Bird_surface_rect.y > 600 or Bird_surface_rect.y < 0:
           pause = True
    screen.fill(black) 
 
    screen.blit(background_surf, background_rect.topleft) 
 
    # screen.blit(instructions_render, instructions_rect.topleft) 
 
    screen.blit(Bird_surface, Bird_surface_rect) 
   # screen.blit(pipe_surface, pipe_rect) 
    while pause:
     Lost_font.render(lost_txt, 100 , red)
     options_font.render(option_txt, 100, red)

   
   
    pygame.display.flip()
   
pygame.quit() 
sys.exit() 

 