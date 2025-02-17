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
    comments = [Comment("hi"), Comment("cool"), Comment("hi"), Comment("hi"), Comment("hi"), Comment("hi"), Comment("hi"), Comment("hi")]
    post = Post("yahli", "tel aviv", "sdfsDF", 32, comments)
    img_post1 = ImagePost("yahli", "tel aviv", "sdfsDF", 32, comments, "Images/ronaldo.jpg")
    text_post = TextPost("yahli", "tel aviv", "sdfsDF", 32, comments, "My post blah blah blah", BLACK, GREY)
    posts_arr = [img_post1, text_post]

    running = True
    current_post = 0
    while running:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(click_post_button, mouse_pos):
                    if current_post == len(posts_arr) - 1:
                        current_post = 0
                    else:
                        current_post += 1
            # like
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(like_button, mouse_pos):
                    posts_arr[current_post].add_like()

            # comment
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(comment_button, mouse_pos):
                    comment = read_comment_from_user()
                    posts_arr[current_post].add_comments(comment)

            # view more comments
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(view_more_comments_button, mouse_pos):
                    draw_comment_text_box()

            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        posts_arr[current_post].display(ui_font, post_font)
        posts_arr[current_post].display_comments()

        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    quit()


main()
