# Class: CSE 1321 
# Section: W04 
# Term: Summer 2024 
# Instructor: Jerry Mamo 
# Group 7 
# Jessica McDonald 
# Cameron Hernandez 

import pygame 
import sys 
import random 
 
pygame.init() 
pygame.mixer.init() 
 
# Sounds 
point_sound = pygame.mixer.Sound("dry-fart.mp3") 
collision_sound = pygame.mixer.Sound("spongebob-fail.mp3") 
win_sound = pygame.mixer.Sound("win.mp3") 
 
# Colors 
black = (0, 0, 0) 
white = (255, 255, 255) 
blue = (0, 0, 255) 
orange = (188, 69, 36) 
pink = (186, 39, 93) 
 
# Display 
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height)) 
 
# Fonts 
small_font = pygame.font.SysFont(None, 35) 
medium_font = pygame.font.SysFont("Comic Sans MS", 40) 
large_font = pygame.font.SysFont(None, 50) 
xl_font = pygame.font.SysFont("Comic Sans MS", 60) 
 
# Background 
background_img = pygame.image.load("FlappyBackround.png").convert() 
background_surf = pygame.transform.scale(background_img, (screen_width + 80, screen_height + 80)) 
background_rect = background_surf.get_rect(topleft=(0, 0)) 
 
# Bird 
bird_size = (60, 45) 
bird_surface = pygame.image.load("bird.png").convert_alpha() 
bird_surface = pygame.transform.scale(bird_surface, bird_size) 
bird_surface_rect = bird_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 10)) 
 
# Clock 
clock = pygame.time.Clock() 

#Main Score Render 
def update_score_surface(point): 
    return medium_font.render("Score: " + str(point), True, pink) 

# Pipes 
def create_pipes(): 
    rand_int = random.randint(200, 400) 
    pipe_gap_surface = pygame.Surface((100, 80), pygame.SRCALPHA) 
    pipe_gap_surface.fill((0, 0, 0, 0)) 
    pipe_gap_rect = pipe_gap_surface.get_rect(centery=rand_int, right=screen_width) 
    bottom_pipe_surface = pygame.Surface((100, 600)) 
    bottom_pipe_rect = bottom_pipe_surface.get_rect(bottomright=(screen_width + 100, screen_height + 100), 
                                                    top=pipe_gap_rect.bottom) 
    top_pipe_surface = pygame.Surface((100, 600)) 
    top_pipe_rect = top_pipe_surface.get_rect(topright=(screen_width + 100, 100), bottom=pipe_gap_rect.top) 
    return [top_pipe_surface, top_pipe_rect, bottom_pipe_surface, bottom_pipe_rect, pipe_gap_surface, pipe_gap_rect, 
            False] 

#Draw
def draw_text(text, font, color, surface, x, y, underline_color=None): 
    text_obj = font.render(text, True, color) 
    text_rect = text_obj.get_rect(center=(x, y)) 
    surface.blit(text_obj, text_rect) 
    if underline_color: 
        underline_rect = pygame.Rect(text_rect.left, text_rect.bottom + 2, text_rect.width, 2) 
        pygame.draw.rect(surface, underline_color, underline_rect) 
 
#Show menu
def show_menu(title, sub_text): 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    return True 
                if event.key == pygame.K_ESCAPE: 
                    pygame.quit() 
                    sys.exit() 
        screen.fill(white) 
        screen.blit(background_surf, background_rect) 
        screen.blit(score_surface, score_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 60))) 
        draw_text(title, xl_font, black, screen, screen_width // 2, screen_height // 4, black) 
        draw_text(sub_text, small_font, black, screen, screen_width // 2, screen_height // 2) 
        draw_text("Press ESC to Quit", small_font, black, screen, screen_width // 2, screen_height // 2 + 50) 
        draw_text("Game Developers: Cameron Hernandez and Jessica McDonald", small_font, black, screen, screen_width // 2, 
                  screen_height - 50) 
        pygame.display.flip() 
        clock.tick(60) 
 
#Show start screen 
def show_start_screen(): 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                return 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP] and bird_surface_rect.top > 0: 
            bird_surface_rect.y -= 4 
        if keys[pygame.K_DOWN] and bird_surface_rect.bottom < screen_height: 
            bird_surface_rect.y += 4 
        screen.fill(black) 
        screen.blit(background_surf, background_rect) 
        screen.blit(bird_surface, bird_surface_rect) 
        draw_text("FLAPPY BIRDS", large_font, orange, screen, screen_width // 2, screen_height // 2 - 225, orange) 
        draw_text("Hold the up and down arrows to move the bird.", small_font, pink, screen, screen_width // 2, 
                  screen_height // 2 - 175) 
        draw_text("Each time you make it through a gap your score will increase.", small_font, pink, screen, 
                  screen_width // 2, screen_height // 2 - 125) 
        draw_text("If you crash into the black your game is over.", small_font, pink, screen, screen_width // 2, 
                  screen_height // 2 - 75) 
        draw_text("If your score reaches 10, you win.", small_font, pink, screen, screen_width // 2, 
                  screen_height // 2 - 25) 
        draw_text("PRESS SPACE TO START", large_font, orange, screen, screen_width // 2, screen_height // 2 + 60) 
        pygame.display.flip() 
        clock.tick(60) 
 
#Main Game  
def main_game(): 
    global bird_surface_rect, pipes, score_surface 
    bird_surface_rect = bird_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 10)) 
    running = True 
    point = 0 
    score_surface = update_score_surface(point) 
    pipes = [create_pipes()] 
    show_start_screen() 
 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r: 
                main_game() 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP] and bird_surface_rect.top > 0: 
            bird_surface_rect.y -= 4 
        if keys[pygame.K_DOWN] and bird_surface_rect.bottom < screen_height: 
            bird_surface_rect.y += 4 
 
        for pipe in pipes: 
            pipe[1].x -= 5 
            pipe[3].x -= 5 
            pipe[5].x -= 5 
 
        if pipes and pipes[-1][1].left == 400: 
            pipes.append(create_pipes()) 
 
        pipes = [pipe for pipe in pipes if pipe[1].right > 0] 
 
        for pipe in pipes: 
            if bird_surface_rect.colliderect(pipe[1]) or bird_surface_rect.colliderect(pipe[3]): 
                collision_sound.play() 
                if show_menu("Game Over", "Press R to Try Again"): 
                    collision_sound.stop() 
                    main_game() 
                else: 
                    running = False 
            if point == 10: 
                win_sound.play(-1) 
                if show_menu("You Won, Congrats!!", "Press R to Restart"): 
                    win_sound.stop() 
                    main_game() 
                else: 
                    running = False 
 
        for pipe in pipes: 
            if not pipe[6] and pipe[1].right - 60 < bird_surface_rect.left: 
                point_sound.play() 
                point += 1 
                score_surface = update_score_surface(point) 
                pipe[6] = True 
 
        screen.fill(black) 
        screen.blit(background_surf, background_rect) 
        screen.blit(bird_surface, bird_surface_rect) 
        for pipe in pipes: 
            screen.blit(pipe[0], pipe[1]) 
            screen.blit(pipe[2], pipe[3]) 
            screen.blit(pipe[4], pipe[5]) 
        screen.blit(score_surface, (30, 30)) 
        draw_text("Press R to Quit/Restart", small_font, blue, screen, screen_width // 5, screen_height - 25) 
        pygame.display.flip() 
        clock.tick(60) 
    pygame.quit() 
    sys.exit() 
 
#Main Game Init 
if __name__ == "__main__": 
    main_game()
