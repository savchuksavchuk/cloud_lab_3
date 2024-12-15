def invert_string(input_string: str) -> str:
    return input_string[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to invert: ")
    print("Inverted string:", invert_string(user_input))
