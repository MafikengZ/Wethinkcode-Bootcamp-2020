import random as rand

num = int(input("Guess a number between 0  and 10: "))

def guesnum (guess):
    randomx = rand.randint(0,10)
    if guess == randomx:
        print("Correct!")
    else:
        print("wrong answer!")


if __name__ == "__main__":
    output = guesnum(num)
    print(f"output: {output}")