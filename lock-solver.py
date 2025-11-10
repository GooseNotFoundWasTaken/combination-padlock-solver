# spin the lock clockwise like 3 times until its smooth and stop on the 0
# pull the shackle. If you are stuck on the 0 when trying to spin clockwise, loosen the tension.
# spin the dial clockwise with your eyes closed and note down the numbers that catch in your head
# change the tension enough to where one number catches on every rotation
# that number is the sticky number
# now to find your guess number(s) between 0 and 11, reset the dial and start on 0
# very tighly pull the shackle on 0. If it wiggles between half numbers, (e.g. 39.5 and 0.5) then it is a guess number.
# Repeat this jiggling process for every number between 0 and 11

stickyNumber = int(input("Sticky number: "))

firstNumber = stickyNumber + 5

remainder = firstNumber % 4

thirdDigitPossibilities = []

for number in list(map(int, input("Guess number(s): ").split())):
    thirdDigitPossibilities.append(number)
    thirdDigitPossibilities.append(number + 10)
    thirdDigitPossibilities.append(number + 20)
    thirdDigitPossibilities.append(number + 30)

for number in thirdDigitPossibilities.copy():
    if number % 4 != remainder:
        thirdDigitPossibilities.remove(number)

thirdDigitPreference = int(input(f"out of {thirdDigitPossibilities} which is the most loose when heavy tenson is applied?: "))

def find_second_digit_possibilities(thirdDigit):
    secondDigitPossibilities = [thirdDigit + 2,
                                (thirdDigit + 10) % 40,
                                (thirdDigit + 18) % 40,
                                (thirdDigit + 26) % 40,
                                (thirdDigit + 34) % 40,
                                (thirdDigit + 6) % 40,
                                (thirdDigit + 14) % 40,
                                (thirdDigit + 22) % 40,
                                (thirdDigit + 30) % 40,
                                (thirdDigit + 38) % 40]

    for number in secondDigitPossibilities.copy():
        if (number - 2) % 40 == thirdDigit or (number + 2) % 40 == thirdDigit:
            secondDigitPossibilities.remove(number)
    return secondDigitPossibilities

digitPairs = {}

for number in thirdDigitPossibilities:
    digitPairs[number] = find_second_digit_possibilities(number)

for secondDigit in digitPairs[thirdDigitPreference]:
    print(f"{firstNumber}-{secondDigit}-{thirdDigitPreference}")

digitPairs.pop(thirdDigitPreference, None)

for thirdDigit in digitPairs:
    for secondDigit in digitPairs[thirdDigit]:
        print(f"{firstNumber}-{secondDigit}-{thirdDigit}")

input("Press Enter to exit...")
