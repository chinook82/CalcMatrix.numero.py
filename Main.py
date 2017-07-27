""" main function of numero calculation of matrix by python """
import datetime
import sys


# --- main def ---
def main(argv):
    calc_date = datetime.datetime.now()
    add_digs = addDigit.AddDigit()

    print("hello this is main function", calc_date.day, calc_date.month, calc_date.year)
# --- main def ---

# --- Call of Main function ---
if __name__ == '__main__':
    main(sys.argv)
