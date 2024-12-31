class Button:
    """
    A class used to represent a Button on the screen
    """
    def __init__(self, x_pos, y_pos, width, height):
        """
        Constructor

        :param x_pos: int
            Position of the top left corner of the button in X axis
        :param y_pos: int
            Position of the top left corner of the button in Y axis
        :param width: int
            Width of button in pixels
        :param height: int
            Height of button in pixels
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
