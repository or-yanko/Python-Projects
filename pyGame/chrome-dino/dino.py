import pygame
import os
import random


# colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# pictures
RUNNING = [pygame.image.load(os.path.join("pics/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("pics/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("pics/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("pics/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("pics/Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("pics/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join(
                    "pics/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("pics/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("pics/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join(
                    "pics/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("pics/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("pics/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("pics/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("pics/Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("pics/Other", "Track.png"))


class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = 8.5
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310

    def update(self, input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = WINDOW_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = WINDOW_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WINDOW_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = Cloud()
    game_speed = 30
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        screen.blit(BG, (x_pos_bg, y_pos_bg))
        screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(WHITE)
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                run = False

        background()

        cloud.draw(screen)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


# constants
WINDOW_WIDTH = 1111
WINDOW_HEIGHT = 590
death_count = 0
points = 0
# init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("dino game")
screen.fill(WHITE)  # fill in white
pygame.display.flip()
finish = False

while not finish:
    screen.fill(WHITE)  # fill in white (default)
    font = pygame.font.Font('freesansbold.ttf', 30)
    if death_count == 0:
        text = font.render("Press any Key to Start", True, BLACK)
    elif death_count > 0:
        text = font.render("Press any Key to Restart", True, BLACK)
        score = font.render("Your Score: " + str(points), True, BLACK)
        scoreRect = score.get_rect()
        scoreRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
        screen.blit(score, scoreRect)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    screen.blit(text, textRect)
    screen.blit(RUNNING[0], (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 - 140))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN:
            main()


pygame.quit()
quit()
