import pygame # pip install pygame (Játékfejlesztő library)
import os # Elérési útvonalak kezelésére használjuk
import math
import random
pygame.mixer.init()
pygame.font.init()

# Ha egy változó csupa nagybetű, akkor azzal jelezzük, hogy ez egy "konstans"
WIDTH = 900
HEIGHT = 500
FPS = 60 # Frames per Second
SPACESHIP_WIDTH = 80    
SPACESHIP_HEIGHT = 80
VELOCITY = 5
MAX_BULLETS = 3
BULLET_VELOCITY = 8

BULLET_WIDTH = 10
BULLET_HEIGHT = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_BULLET_COLOR = (255, 255, 0) # RGB (Red, Green, Blue)
RED_BULLET_COLOR = (255, 0, 0)
BORDER_COLOR = (0, 0, 0) # Fekete 
FONT_COLOR = (255, 255, 255) # Fehér

clock = pygame.time.Clock() # Clock osztályát példányosítjuk

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War") # Ablak neve

# Határozzuk meg annak a fájlnak a mappáját ami éppen fut
ASSETS_PATH = os.path.dirname(os.path.abspath(__file__)) # space_war mappa
ASSETS_PATH = os.path.join(ASSETS_PATH, "assets")

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "laser.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "explosion.wav"))

HEALTH_FONT = pygame.font.SysFont("Arial", 40)

BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 270)

def draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    window.blit(BACKGROUND, (0, 0))
    
    border_width = 10
    border = pygame.Rect(WIDTH // 2 - border_width // 2, 0, border_width, HEIGHT)
    pygame.draw.rect(window, BORDER_COLOR, border)
    
    red_health_text = HEALTH_FONT.render("Health " + str(red_health), True, FONT_COLOR)
    yellow_health_text = HEALTH_FONT.render("Health " + str(yellow_health), True, FONT_COLOR)
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))
    
    window.blit(RED_SPACESHIP, (red.x, red.y))
    window.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(window, RED_BULLET_COLOR, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW_BULLET_COLOR, bullet)
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

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if bullet.x < 0:
            red_bullets.remove(bullet)
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            
def draw_winner(text):
    font = pygame.font.SysFont("Arial", 100)
    text_surface = font.render(text, True, FONT_COLOR)
    left = WIDTH // 2 - text_surface.get_width() // 2
    top = HEIGHT // 2 - text_surface.get_height() // 2
    window.blit(text_surface, (left, top))
    pygame.display.update()
    pygame.time.delay(5000) # 5 mp-es várakozás

def main():
    red = pygame.Rect(WIDTH - 150, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    while True:
        clock.tick(FPS) # 60 - 1 másodperc 60-ad részét várakozunk
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                HIT_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                HIT_SOUND.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and MAX_BULLETS > len(yellow_bullets):
                    bullet = pygame.Rect(yellow.x + SPACESHIP_WIDTH,
                                         yellow.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2,
                                         BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and MAX_BULLETS > len(red_bullets):
                    bullet = pygame.Rect(red.x - BULLET_WIDTH,
                                         red.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2,
                                         BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
        keys_pressed = pygame.key.get_pressed()
        red_control(keys_pressed, red)
        yellow_control(keys_pressed, yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
        if red_health <= 0:
            draw_winner("Yellow Wins!")
            break
        if yellow_health <= 0:
            draw_winner("Red Wins!")
            break
        
# Ez lesz a program belépési pontja
if __name__ == "__main__":
    main()