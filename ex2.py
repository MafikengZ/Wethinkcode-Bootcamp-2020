number = int(input("Number: "))

def collatz (n):
    """
    func checks if the input number is even and returns division by 2
    else (3 * n + 1)
    Arg:(int n) input number
    """
    if n % 2 ==0:       #modulus operator % checks the remainder 
        result = n // 2
        print(result)
    else:
        result = (3 * n) + 1
        print(result)

if __name__ == "__main__":
    output = collatz(number)
    output