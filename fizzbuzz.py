def fizz_buzz(number: int) -> str:
    """
    Play FizzBuzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3,
        'buzz' if the number is divisible by 5, and
        ;fizzbuzz' if the number is divisible by 3 and 5.
        The number as a string otherwise
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return str(number)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose. The correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))

