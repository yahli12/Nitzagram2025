import pygame
from buttons import *
from constants import *
from helpers import *


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description, likes_counter, comments): #TODO: add parameters
        #TODO: write me!
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = comments
        self.comments_display_index = 4

    def add_like(self):
        self.likes_counter += 1

    def add_comments(self, comment):
        self.comments.append(comment)

    def display(self, ui_font, post_font):
        # TODO: write me!
        username_text = ui_font.render(f"{self.username}", True, BLACK)
        location_text = ui_font.render(f"{self.location}", True, BLACK)
        like_text = ui_font.render(f"{self.likes_counter}", True, BLACK)
        description_text = ui_font.render(f"{self.description}", True, BLACK)

        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        screen.blit(like_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_comments(self, ui_font):
        """
        Displays up to NUM_OF_COMMENTS_TO_DISPLAY comments at a time.
        If there are more than NUM_OF_COMMENTS_TO_DISPLAY, a "View More Comments" button is displayed.
        """
        view_more_comments_text = ui_font.render("View more comments", True, GREY)
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            screen.blit(view_more_comments_text, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        comment_y_pos = FIRST_COMMENT_Y_POS
        for i in range(min(len(self.comments), NUM_OF_COMMENTS_TO_DISPLAY)):
            comment_text = ui_font.render(self.comments[i], True, BLACK)
            screen.blit(comment_text, (FIRST_COMMENT_X_POS, comment_y_pos))
            comment_y_pos += COMMENT_LINE_HEIGHT
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(view_more_comments_button, mouse_pos):
                    draw_comment_text_box()


class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments, image):
        super().__init__(username, location, description, likes_counter, comments)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self, ui_font, post_font):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        super().display(ui_font, post_font)

    def display_comments(self, ui_font):
        super().display_comments(ui_font)


class TextPost(Post):
    def __init__(self, username, location, description, likes_counter, comments, text, text_color, background_color):
        super().__init__(username, location, description, likes_counter, comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.font = pygame.font.SysFont("chalkduster.ttf", TEXT_POST_FONT_SIZE)

    def display(self, ui_font, post_font):
        post_background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, post_background)
        text_lines = from_text_to_array(self.text)
        line_number = 0

        for line in text_lines:
            text = self.font.render(line, True, self.text_color)
            text_pos = center_text(len(text_lines), text, line_number)
            screen.blit(text, text_pos)
            line_number += 1
        super().display(ui_font, post_font)

    def display_comments(self, ui_font):
        super().display_comments(ui_font)
