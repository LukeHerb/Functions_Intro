import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The string that the user will see, when
        they're prompted.
    :return: The integer the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is an invalid input".format(temp))


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0
print(f"Please guess a number between 1 and {highest}: ")

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print(f"{guess} is correct")
    else:
        if guess < answer:
            print(f"{guess} is incorrect, please guess higher")
        else:   # Must be higher
            print(f"{guess} is incorrect, please guess lower")


