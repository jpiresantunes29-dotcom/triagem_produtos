def read_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("Please enter an integer greater than zero.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_non_negative_integer(message):
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            else:
                print("Please enter an integer greater than or equal to zero.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_non_negative_float(message):
    while True:
        try:
            value = float(input(message))
            if value >= 0:
                return value
            else:
                print("Please enter a value greater than or equal to zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_yes_or_no(message):
    while True:
        value = input(message).strip().lower()
        if value == "yes" or value == "no":
            return value
        else:
            print("Invalid input. Please enter yes or no.")
