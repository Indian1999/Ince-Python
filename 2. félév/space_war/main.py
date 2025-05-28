import pygame # pip install pygame (Játékfejlesztő library)
import os # Elérési útvonalak kezelésére használjuk
import math
import random

# Ha egy változó csupa nagybetű, akkor azzal jelezzük, hogy ez egy "konstans"
WIDTH = 900
HEIGHT = 500
FPS = 60 # Frames per Second
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 80
VELOCITY = 5

clock = pygame.time.Clock() # Clock osztályát példányosítjuk

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War") # Ablak neve

# Határozzk meg annak a fájlnak a mappáját ami éppen fut
ASSETS_PATH = os.path.dirname(os.path.abspath(__file__)) # space_war mappa
ASSETS_PATH = os.path.join(ASSETS_PATH, "assets")

BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 270)

def draw_frame(red, yellow):
    window.blit(BACKGROUND, (0, 0))
    
    window.blit(RED_SPACESHIP, (red.x, red.y))
    window.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    
    pygame.display.update()
    
def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x >= WIDTH // 2 + VELOCITY:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y >= 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_HEIGHT:
        red.y += VELOCITY

def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_w] and yellow.y >= 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_HEIGHT:
        yellow.y += VELOCITY
    if keys_pressed[pygame.K_a] and yellow.x >= 0:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x  <= WIDTH // 2 - SPACESHIP_WIDTH:
        yellow.x += VELOCITY

def main():
    red = pygame.Rect(WIDTH - 150, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    while True:
        clock.tick(FPS) # 60 - 1 másodperc 60-ad részét várakozunk
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys_pressed = pygame.key.get_pressed()
        red_control(keys_pressed, red)
        yellow_control(keys_pressed, yellow)
        draw_frame(red, yellow)
        
# Ez lesz a program belépési pontja
if __name__ == "__main__":
    main()