from random import randint


n = int(input("Range from 1 to >>: "))
print(f"Think of a number between 1 and {n}")
randnumber = randint(1,n) # a random number in a range between 1 to 5


def guessnumber ():
    """
    guess a number in a given range 
    Args:(int n) input number from user
    """
    
    counter = 1
    while True:
        number = int(input("Guess a number: "))
        if number < randnumber:
            print("Your guess too low")
        elif number > randnumber:
            print("Your Guess too high")
        elif number == randnumber:
            print(f"Good guess! You guessed your number {counter} tries")
            break
        counter += 1
        
    

if __name__ == "__main__":
    output = guessnumber()
    output