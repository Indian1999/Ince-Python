import pygame
import random
pygame.font.init()

SNAKE_COLOR = (0,0,0) # fekete
FOOD_COLOR = (0, 255, 0) # zöld
BACKGROUND_COLOR = (0, 0, 255) # kék
SCORE_COLOR = (255, 255, 255) # fehér
GAME_OVER_COLOR = (255, 0, 0) # piros

# Érdemes úgy, hogy sok közös osztójuk legyen
WIDTH = 1000
HEIGHT = 500
PIXEL_SIZE = 50 # WIDTH és HEIGHT-ot osztja
SPEED = 6 # FPS  

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()

game_over_font = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 25)

def random_pos():
    x = random.randrange(0, WIDTH, PIXEL_SIZE) # 0, 20, 40, 60, ...., WIDTH - 20
    y = random.randrange(0, HEIGHT, PIXEL_SIZE)
    return x, y

def draw_snake(snake):
    for pixel in snake:
        pygame.draw.rect(window, SNAKE_COLOR, (pixel[0], pixel[1], PIXEL_SIZE, PIXEL_SIZE))

def gameloop():
    game_over = False
    application_close = False
    
    # osztunk és szorzunk is a PIXEL_SIZE-al, hogy pont egy pixelen helyezkedjen el
    x_snake = round(WIDTH // 2 / PIXEL_SIZE) * PIXEL_SIZE
    y_snake = round(HEIGHT // 2 / PIXEL_SIZE) * PIXEL_SIZE

    # a kígyó x és y irányú sebességei (-1, 0, 1)
    x_change = 0
    y_change = 0
    
    snake = []
    length_of_snake = 1
    
    x_food, y_food = random_pos() # visszaad egy random pixel koordinátát
    while not application_close:
        clock.tick(SPEED)
        
        while game_over:
            window.fill(BACKGROUND_COLOR)
            text = game_over_font.render("R: újraindítás | Q: kilépés", True, GAME_OVER_COLOR)
            window.blit(text, (WIDTH // 2 - text.get_width() // 2,
                               HEIGHT // 2 - text.get_height() // 2))
            
            score_text = score_font.render(f"Score: {length_of_snake - 1}", True, SCORE_COLOR)
            window.blit(score_text, (5,5))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_r:
                        gameloop()
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                application_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -PIXEL_SIZE
                    y_change = 0
                if event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = PIXEL_SIZE
                    y_change = 0
                if event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -PIXEL_SIZE
                if event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = PIXEL_SIZE
        
        #Leellenőrzzük, hogy nekiment-e a falnak a kígyó
        if x_snake >= WIDTH or x_snake < 0 or y_snake < 0 or y_snake >= HEIGHT:
            game_over = True
            continue # A következő ciklus iterációra ugrik
        
        x_snake += x_change
        y_snake += y_change
        
        window.fill(BACKGROUND_COLOR) # háttér legyen kék
        pygame.draw.rect(window, FOOD_COLOR, (x_food, y_food, PIXEL_SIZE, PIXEL_SIZE))
        
        snake.append([x_snake, y_snake])
        if len(snake) > length_of_snake:
            del snake[0]
            
        for pixel in snake[:-1]: # a kigyónak a fejét nem ellenőrizzük
            if pixel == snake[-1]:
                game_over = True
                break
        
        draw_snake(snake)
        
        # Ha a kígyó feje a kajánál van, egye meg
        if x_snake == x_food and y_snake == y_food:
            x_food, y_food = random_pos()
            length_of_snake += 1
            
        score_text = score_font.render(f"Score: {length_of_snake - 1}", True, SCORE_COLOR)
        window.blit(score_text, (5,5))
        
        pygame.display.update()
    
    pygame.quit()
    exit()

if __name__ == "__main__": # A program belépési pontja
    gameloop()