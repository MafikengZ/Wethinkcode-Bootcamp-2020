num1 = float(input("value1: "))
num2 = float(input("value: "))
num3 = float(input("value: "))

def average (x ,y , z):
    """
    calculate the aveage of 3 values
    Args: three input values
    retuns: (float value)
    """
    numberlist = [x,y,z]
    mean = sum(numberlist) / len(numberlist)
    return mean

if __name__ == "__main__":

    avg = average(num1, num2 , num3)
    print(f"Th average is {str(avg)}")