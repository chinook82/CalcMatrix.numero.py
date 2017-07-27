""" Class for 4 additional Digits class """
import AddDigit.AddDigit as AD, datetime


class AddDigits:
    AD_01 = AD.AddDigit(1)
    AD_02 = AD.AddDigit(2)
    AD_03 = AD.AddDigit(3)
    AD_04 = AD.AddDigit(4)

    def __init__(self, value):
        self.AD_01 = AD.AddDigit.set_add_digit(value, 1, "AD_01")
        self.AD_02 = AD.AddDigit.set_add_digit(value, 2, "AD_02")
        self.AD_02 = AD.AddDigit.set_add_digit(value, 3, "AD_03")
        self.AD_02 = AD.AddDigit.set_add_digit(value, 4, "AD_04")
        pass
    # __init__ def

    def add_digits(self):
        pass
    # add_digits def

# aDigits class


