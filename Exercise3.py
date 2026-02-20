# ANSI colors for terminal output
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


# Custom Exceptions
class ValueTooSmallError(Exception):
    def __init__(self, value, message):
        super().__init__(message)  # stores in args
        self.value = value
        self.message = message

    def __str__(self):
        return f"{RED}ValueTooSmallError: The value {self.value} is {self.message}{RESET}"


class ValueTooLargeError(Exception):
    def __init__(self, value, message):
        super().__init__(message)
        self.value = value
        self.message = message

    def __str__(self):
        return f"{YELLOW}ValueTooLargeError: The value {self.value} is {self.message}{RESET}"


class NoMultipleOfFiveError(Exception):
    def __init__(self, value, message):
        super().__init__(message)
        self.value = value
        self.message = message

    def __str__(self):
        return f"{BLUE}NoMultipleOfFiveError: The value {self.value} is {self.message}{RESET}"


def get_integer():
    while True:
        try:
            value = input("Enter an integer number:\n")
            if value == "":
                raise ValueError(f"{RED}No digits entered{RESET}")
            elif not value.isdigit():  # strict digits only
                raise ValueError(f"{RED}Wrong input. Only digits please{RESET}")

            x = int(value)

            # Custom rules
            if x < 100:
                raise ValueTooSmallError(x, "< 100")
            elif x > 200:
                raise ValueTooLargeError(x, "> 200")
            elif x % 5 != 0:
                raise NoMultipleOfFiveError(x, "not multiple of 5")

        except (ValueTooSmallError, ValueTooLargeError, NoMultipleOfFiveError) as e:
            print(e)
        except ValueError as e:
            print(e)
        else:
            return x
        finally:
            # εδώ μπορείς να προσθέσεις cleanup αν χρειάζεται
            pass


# Εκτέλεση
num = get_integer()
print(f"Valid number entered: {num}")