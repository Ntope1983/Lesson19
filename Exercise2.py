# Try Except else finally example
def get_integer():
    while True:
        try:
            value = input(f"Enter an integer number\n")
            if value == "":
                raise ValueError("No digits entered")
            elif not value.isdigit():
                raise ValueError("Wrong Input.Only digits please")
            x = int(value)
        except Exception as e:
            print("Exception()", str(e))
        else:
            print("else block")
            return x
        finally:
            print("Finally block")
            pass


get_integer()
