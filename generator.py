import random

answer = input("Enter a valid pangram: ")

puzzle = list(dict.fromkeys(answer))
random.shuffle(puzzle)
print(puzzle)
