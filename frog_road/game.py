import pygame
import sys
import random
from bird import Bird
from street import Street
from river import River
from berry import Berry
# Add the files from your computer: git add .
# Commit the files to GitHub: git commit -m "message"
# git push
pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Frog Road!')
CLOCK = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 80, 175)
FONT = pygame.font.Font('resources/joystix monospace.ttf', 20)
MENU_BIG = pygame.font.Font('resources/joystix monospace.ttf', 60)
MENU_MED = pygame.font.Font('resources/joystix monospace.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/joystix monospace.ttf', 15)
MENU_IMAGE = pygame.image.load('resources/New Piskel (3).png')
START_MENU = True
END_MENU = False
bird = Bird()
number_of_berries = 5
berries = []
for _ in range(number_of_berries):
    berries.append(Berry((random.randint(0, WIDTH - Berry.SIZE[0]), random.randint(60, HEIGHT - Berry.SIZE[1]))))


streets = []
number_of_buses = 1
street_height = 400


for _ in range(2):
    streets.append(Street(street_height, 'Left', random.randint(1, number_of_buses)))
    streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_buses)))
    street_height -= 80

rivers = []
number_of_logs = 3
number_of_alligators = 1
river_height = 200
for _ in range(2):
    rivers.append(River(river_height, 'Left', random.randint(1, number_of_logs), random.randint(0, number_of_alligators)))
    rivers.append(River(river_height - 30, 'Right', random.randint(1, number_of_logs), random.randint(0, number_of_alligators)))
    river_height -= 60


score = 0
current_best = 0
high_score = 0
while True:
    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(BLUE)
        # Show text on menu screen
        name = MENU_BIG.render('BIRD ROAD', True, WHITE)
        instructions = MENU_SMALL.render('Press Space To Start', True, WHITE)
        SCREEN.blit(name, (75, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 170))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print("Space?")
                if event.key == pygame.K_SPACE:
                    START_MENU = False
        pygame.display.update()

    while END_MENU:
        # Tick forward at 15 frames per second
        CLOCK.tick(15)

        SCREEN.fill(BLUE)

        # Show text on menu screen
        thx = MENU_MED.render('Thanks for Playing!', True, WHITE)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(instructions, (130, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END_MENU = False
                    current_best = 0
                    score = 0
                    bird.lives = 3

        pygame.display.update()

    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                bird.move_up()
            if event.key == pygame.K_a:  # A
                bird.move_left()
            if event.key == pygame.K_s:  # S
                bird.move_down()
            if event.key == pygame.K_d:  # D
                bird.move_right()

    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for bus in street.buses:
            SCREEN.blit(bus.image, bus.rect)
            bus.move()
            if bird.rect.colliderect(bus.rect):
                bird.reset_position()

    bird_on_log = False  # new
    for river in rivers:
        # Draw River
        SCREEN.fill(BLUE, river.rect)


                # Log
        for log in river.logs:
            SCREEN.blit(log.image, log.rect)
            log.move()
            if bird.rect.colliderect(log.rect):
                bird.move_on_log(log)
                bird_on_log = True  # new
        for alligator in river.alligators:
            SCREEN.blit(alligator.image, alligator.rect)
            alligator.move()
            if bird.rect.colliderect(alligator.rect):
                bird.reset_position()

        # Collided with River and not a Log - new
        if not bird_on_log and bird.rect.colliderect(river.rect):
            bird.reset_position()
    for berry in berries:
        SCREEN.blit(berry.image, berry.rect)
        if bird.rect.colliderect(berry.rect):
            score += 250
            berries.remove(berry)

    if 475-bird.rect.top > current_best:
        current_best = 475 - bird.rect.top
    if score + current_best >= high_score:
        high_score = score + current_best
    if bird.rect.top <= 60:
        if bird.rect.top <= 60:
            bird.reset_position()
            bird.lives += 1
            current_best = 0
            score += 1000 + current_best

    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(bird.lives), True, WHITE)

    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))
    SCREEN.blit(bird.image, bird.rect)

    if bird.lives == 0:
        END_MENU = True

    pygame.display.update()
    pygame.display.flip()
