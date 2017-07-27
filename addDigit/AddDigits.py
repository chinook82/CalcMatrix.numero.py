""" Class for 4 additional Digits class """
import AddDigit, datetime


class AddDigits:
    aDig1 = AddDigit.AddDigit(datetime.date.today(),"current day")
    aDig2 = AddDigit.AddDigit(datetime.date.today(),"current day")
    aDig3 = AddDigit.AddDigit(datetime.date.today(),"current day")
    aDig4 = AddDigit.AddDigit(datetime.date.today(),"current day")

    def __init__(self, value, description):
        self.aDig1 = AddDigit.AddDigit(value, description)
        pass
    # __init__ def

    def add_digits(self):
        pass
    # add_digits def

# aDigits class


