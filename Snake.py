import pygame, random
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('SNAKE GAME')

#setting the FPS and the clock
FPS = 20
clock = pygame.time.Clock()

#setting the game values 

SNAKE_SIZE = 20
head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

score = 0

snake_dy = 0
snake_dx = 0

#setting the color values to make things easier

GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
DARKRED = (150,0,0)
BLACK = (0,0,0)
DARKGREEN = (10,50,10)

#setting up the font for the game which will be the system font itself

font = pygame.font.SysFont("gabriola", 50)

#creating texts 

title_text = font.render("SNAKE", True, GREEN, BLACK)
title_text_rect = title_text.get_rect()
title_text_rect.topright = (WINDOW_HEIGHT-50, 10)
score_text = font.render("Score: "+ str(score), True, GREEN, BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)
game_over_text = font.render("GAME OVER", True, RED, BLACK)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_HEIGHT//2, WINDOW_WIDTH//2)
continue_text = font.render("Press any key to continue", True, RED, BLACK)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_HEIGHT//2  , WINDOW_WIDTH//2 +64)

#loading the sound effect in the game when snake collides with the red object

sound1 = pygame.mixer.Sound('pick_up_sound.wav')

#setting images(in this game I am not using any images but I am using the rects to form a simple looking snake and food)

apple_coord = (500,500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display, RED, apple_coord)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display, GREEN, head_coord)
body_coords = [] 




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #moving the snake according to the user given directions via KEYDOWN
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    #adding the head coordinate to the first index of the list created above.
    #This will move all of the snakes body by one position in the list

    body_coords.insert(0, head_coord)
    body_coords.pop()

    #updating the x and y coordinate of the snake

    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    #Game over 

    if head_rect.left<0 or head_rect.right>WINDOW_WIDTH or head_rect.top<0 or head_rect.bottom>WINDOW_HEIGHT or head_coord in body_coords:
        display.blit(game_over_text, game_over_text_rect)
        display.blit(continue_text, continue_text_rect)
        pygame.display.update()

        is_paused = True

        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT//2
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0

                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #setting the collision between the snake and the apple

    if head_rect.colliderect(apple_rect):
        score += 1
        sound1.play()

        #removing the apple from the cuurent position after the positon and randomly placing it anywhere on the screen
        
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y =random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        body_coords.append(head_coord)

        score_text = font.render("Score: "+ str(score), True, GREEN, BLACK)

    display.fill(WHITE)

    display.blit(title_text, title_text_rect)
    display.blit(score_text, score_text_rect)

    for body in body_coords:
        pygame.draw.rect(display, GREEN, body)

    head_rect = pygame.draw.rect(display, DARKGREEN, head_coord)
    apple_rect = pygame.draw.rect(display, RED, apple_coord)


    clock.tick(FPS)
    pygame.display.update()
pygame.quit()