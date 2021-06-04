import pygame
import time
import random

class Snake:
    WHITE = (255,255,255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WIDTH = 720
    HEIGHT = 480

    SNAKE_SPEED = 20
    BLOCK_SIZE = 10

    RECORD = 0

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")
        self.playGame(screen)
    
    def playGame(self, screen: pygame.Surface) -> None:
        gameOver = False
        x = self.WIDTH/2
        y = self.HEIGHT/2
        xChange = 0
        yChange = 0
        snakeList = []
        lengthSnake = 1
        foodx = round(random.randrange(0, self.WIDTH - self.BLOCK_SIZE) / 10.0) * 10.0
        foody = round(random.randrange(0, self.HEIGHT - self.BLOCK_SIZE) / 10.0) * 10.0
        clock = pygame.time.Clock()
        fontStyle1 = pygame.font.SysFont("papyrus", 50)
        fontStyle2 = pygame.font.SysFont("papyrus", 40)
        prevEvent = ""
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and prevEvent != "right":
                        xChange = -self.BLOCK_SIZE
                        yChange = 0
                        prevEvent = "left"
                    elif event.key == pygame.K_RIGHT and prevEvent != "left":
                        xChange = self.BLOCK_SIZE
                        yChange = 0
                        prevEvent = "right"
                    elif event.key == pygame.K_UP and prevEvent != "down":
                        xChange = 0
                        yChange = -self.BLOCK_SIZE
                        prevEvent = "up"
                    elif event.key == pygame.K_DOWN and prevEvent != "up":
                        xChange = 0
                        yChange = self.BLOCK_SIZE
                        prevEvent = "down"

            if x >= self.WIDTH or x < 0 or y >= self.HEIGHT or y < 0:
                gameOver = True
                if self.RECORD < lengthSnake-1:
                    self.RECORD = lengthSnake-1
            
            x += xChange
            y += yChange
            screen.fill(self.BLACK)
            pygame.draw.rect(screen, self.RED, [foodx, foody, self.BLOCK_SIZE, self.BLOCK_SIZE])
            snakeHead = []
            snakeHead.append(x)
            snakeHead.append(y)
            snakeList.append(snakeHead)
            if len(snakeList) > lengthSnake:
                del snakeList[0]
            
            for segment in snakeList[:-1]:
                if segment == snakeHead:
                    gameOver = True
                    if self.RECORD < lengthSnake - 1:
                        self.RECORD = lengthSnake - 1
            self.currSnake(self.BLOCK_SIZE, snakeList, screen)
            self.scoreCount(lengthSnake-1, screen)
            self.recordCount(screen)
            pygame.display.update()
            if x == foodx and y == foody:
                foodx = round(random.randrange(0, self.WIDTH - self.BLOCK_SIZE) / 10.0) * 10.0
                foody = round(random.randrange(0, self.HEIGHT - self.BLOCK_SIZE) / 10.0) * 10.0
                lengthSnake += 1

            clock.tick(self.SNAKE_SPEED)
        screen.fill(self.BLACK)
        self.displayMessage("Game Over", self.RED, fontStyle1, screen, "center")
        self.displayMessage("Press 'r' to restart or 'Esc' to exit.", self.RED, fontStyle2, screen, "below")
        pygame.display.update()
        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        restart = True
        self.playGame(screen)

    def displayMessage(self, message: str, colour: str, fontStyle: str, screen: pygame.Surface, position: str) -> None:
        msg = fontStyle.render(message, True, colour)
        if position == "center":
            screen.blit(msg, [self.WIDTH/2 - self.WIDTH*0.18, self.HEIGHT/2 - self.HEIGHT*0.15])
        elif position == "below":
             screen.blit(msg, [self.WIDTH*0.1, self.HEIGHT/2])
    
    def currSnake(self, blockSize: int, lengthSnake, screen):
        for segment in lengthSnake:
            pygame.draw.rect(screen, self.WHITE, [segment[0], segment[1], blockSize, blockSize])
    
    def scoreCount(self, score, screen):
        val = pygame.font.SysFont("papyrus", 30).render("Current score: " + str(score), True, (255,255,0))
        screen.blit(val, [0,0])
    
    def recordCount(self, screen):
        val = pygame.font.SysFont("papyrus", 30).render("Record score: " + str(self.RECORD), True, (255, 255, 0))
        screen.blit(val, [0, 40])

def main():
    game = Snake()

if __name__ == "__main__":
    main()