import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    time.sleep(1)

    screen.fill("purple")

    screen.fill("green")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()