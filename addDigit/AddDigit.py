""" Class for additional Digit """
import datetime


class AddDigit:
    value = 0
    description = ""
    position = 0

    def __init__(self):
        self.value = datetime.date.today()
        self.position = 0
        self.description = "AD"
    pass
    # init def

    def set_add_digit(self, value, position, description):
        self.value = value
        self.position = position
        self.description = description
        pass
    # set_add_digit def

    def get_add_digit(self):
        return self
    # get_add_digit def

    def get_value(self):
        return self.value
    # get_value def

    def get_description(self):
        return self.description
    # get_description def

    def get_position(self):
        return self.position
    # get_position def

# AddDigit class
