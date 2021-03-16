num1 = int(input("value1: "))
num2 = int(input("value: "))
num3 = int(input("value: "))

def sumequal (x , y , z):
    """
    calculate sum of three values if two values are equal retuns Null
    Args: (int values)
    """
    intnum = list([x,y,z])
    if len(set(intnum)) == len(intnum): #if lengths are equal and we have no duplicate
       return sum(intnum)
    else:
        return 0

if __name__ == "__main__":
    output = sumequal(num1, num2 , num3)
    print(f"output: {output}")