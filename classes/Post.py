import pygame
from constants import *
from helpers import *
from buttons import *


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, ui_font, y_pos):

        comment_text = ui_font.render(self.text, True, BLACK)
        screen.blit(comment_text, (FIRST_COMMENT_X_POS, y_pos))


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

    def add_comments(self, text):
        new_comment = Comment(text)
        self.comments.append(new_comment)

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

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        ui_font = pygame.font.SysFont(None, UI_FONT_SIZE)
        y_pos = FIRST_COMMENT_Y_POS
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(ui_font,y_pos)
            position_index += 1
            y_pos += COMMENT_LINE_HEIGHT
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break


class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments, image):
        super().__init__(username, location, description, likes_counter, comments)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self, ui_font, post_font):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        super().display(ui_font, post_font)

    def display_comments(self):
        super().display_comments()


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

    def display_comments(self):
        super().display_comments()
