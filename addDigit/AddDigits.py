""" Class for 4 additional Digits class """


class AddDigits:
    AD_01 = addDigit.AddDigit(1)
    AD_02 = addDigit.AddDigit(2)
    AD_03 = addDigit.AddDigit(3)
    AD_04 = addDigit.AddDigit(4)

    def __init__(self, value):
        self.AD_01 = addDigit.AddDigit.set_add_digit(value, 1, "AD_01")
        self.AD_02 = addDigit.AddDigit.set_add_digit(value, 2, "AD_02")
        self.AD_02 = addDigit.AddDigit.set_add_digit(value, 3, "AD_03")
        self.AD_02 = addDigit.AddDigit.set_add_digit(value, 4, "AD_04")
        pass
    # __init__ def

    def add_digits(self):
        pass
    # add_digits def

# aDigits class


