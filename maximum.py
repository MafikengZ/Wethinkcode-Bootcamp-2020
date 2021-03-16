value1 = int(input("value: "))
value2 = int(input("value: "))

# maximun value between two input values
def maxvalue (a , b):
    if a >= b:
        return a
    else:
        return b

if __name__ == "__main__":
    output = maxvalue(value1 , value2)
    print(f"Maximum value between {value1} and {value2} is {output}")