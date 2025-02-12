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
    post = Post("yahli", "tel aviv", "sdfsDF", 32, ["ASDWDA", "hello", "nice", "amazing", "cool", "good"])
    img_post1 = ImagePost("yahli", "tel aviv", "sdfsDF", 32, ["ASDWDA", "hello", "nice", "amazing", "cool", "good"], "Images/ronaldo.jpg")
    text_post = TextPost("yahli", "tel aviv", "sdfsDF", 32, ["ASDWDA", "hello", "nice", "amazing", "cool"], "My post blah blah blah", BLACK, GREY)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        img_post1.display(ui_font, post_font)
        img_post1.display_comments(ui_font)

        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    quit()


main()
