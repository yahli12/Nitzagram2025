# Create Buttons: like, comment, change_image, view more comments
from classes.Button import Button
from constants import *

like_button = Button(LIKE_BUTTON_X_POS,
                     LIKE_BUTTON_Y_POS,
                     LIKE_BUTTON_WIDTH,
                     LIKE_BUTTON_HEIGHT)
comment_button = Button(COMMENT_BUTTON_X_POST,
                        COMMENT_BUTTON_Y_POS,
                        COMMENT_BUTTON_WIDTH,
                        COMMENT_BUTTON_HEIGHT)
click_post_button = Button(POST_X_POS,
                           POST_Y_POS,
                           POST_WIDTH,
                           POST_HEIGHT)
view_more_comments_button = Button(VIEW_MORE_COMMENTS_X_POS,
                                   VIEW_MORE_COMMENTS_Y_POS,
                                   VIEW_MORE_COMMENT_WIDTH,
                                   VIEW_MORE_COMMENT_HEIGHT)
