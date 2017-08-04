""" Class for 4 additional Digits class """
from addDigit.AddDigit import AddDigit


class AddDigits:
    AD_01 = AddDigit(1)
    AD_02 = AddDigit(2)
    AD_03 = AddDigit(3)
    AD_04 = AddDigit(4)
    description = ""

    def __init__(self):
        self.AD_01.set_add_digit(0, 1, "AD_01")
        self.AD_02.set_add_digit(0, 2, "AD_02")
        self.AD_03.set_add_digit(0, 3, "AD_03")
        self.AD_04.set_add_digit(0, 4, "AD_04")
        pass
    # __init__ def

    def calc_digits(self, calc_date):
        tmp_day = calc_date.day
        while tmp_day >= 10:
            self.AD_01.value += tmp_day % 10
            tmp_day //= 10
            pass
        # end while
        self.AD_01.value = self.AD_01.value + tmp_day

        tmp_month = calc_date.month

        while tmp_month >= 10:
            self.AD_01.value += tmp_month % 10
            tmp_month //= 10
            pass
        # end while
        self.AD_01.value = self.AD_01.value + tmp_month

        tmp_year = calc_date.year
        while tmp_year >= 10:
            self.AD_01.value += tmp_year % 10
            tmp_year //= 10
            pass
        # end while
        self.AD_01.value = self.AD_01.value + tmp_year

        tmp_AD = self.AD_01.value
        while tmp_AD >= 10:
            self.AD_02.value += tmp_AD % 10
            tmp_AD //= 10
            pass
        # end while
        self.AD_02.value = self.AD_02.value + tmp_AD

        self.AD_03.value = self.AD_01.value - 2 * tmp_day

        tmp_AD = self.AD_03.value
        while tmp_AD >= 10:
            self.AD_04.value += tmp_AD % 10
            tmp_AD //= 10
            pass
        # end while
        self.AD_04.value = self.AD_04.value + tmp_AD
        pass
    # calc_digits def

    def add_digits(self):

        pass
    # add_digits def
# aDigits class


