def get_integer():
    while True:
        try:
            value = input(f"Enter an integer number\n")
            if value == "":
                raise ValueError("No digits entered")
            elif not value.isdigit():
                raise ValueError("Wrong Input.Only digits please")
            x=int(value)
        except Exception as e:
            print("Exception()", str(e))
        else:
            return x


print(get_integer())
