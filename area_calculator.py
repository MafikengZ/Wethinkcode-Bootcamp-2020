
num1 = float(input("Length: "))
num2 = float(input("Width: "))
def area (length , width):
    """
    calcualtes the area (l * w)
    Args:
        length: (float) 
        width:(float)
    return: (float) value
    """
    results = length * width
    return results

if __name__ == "__main__":
    rectangle = area(num1 , num2)
    print(f"The are of a rectangle is {str(rectangle)}")