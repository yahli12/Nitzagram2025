import pygame
from helpers import *
from constants import *
from classes.Post import *


def main():

    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))

    ui_font = pygame.font.SysFont(None, UI_FONT_SIZE)
    post_font = pygame.font.SysFont(None, TEXT_POST_FONT_SIZE)

    # TODO: add a post here
    post = Post("yahli", "tel aviv", "sdfsDF", 32, ["ASDWDA", "ASDWA"])
    img_post1 = ImagePost("yahli", "tel aviv", "sdfsDF", 32, ["ASDWDA", "ASDWA"], "Images/ronaldo.jpg")

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        img_post1.display(ui_font, post_font)

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
