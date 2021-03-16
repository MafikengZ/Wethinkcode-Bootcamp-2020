ferenheit = float(input("Farenheit: "))

def convert (degrees):
    """
    convert degree F to Degree celsius (32F - 32) * 5/9
    Args: (float | int value)Degrees Farenheit
    returns:(numeric value) celsius
    """
    celsius = (degrees - 32 )* 5/9
    return celsius

if __name__ == "__main__":
     output = convert (ferenheit)
     print(f"{str(output)} celsius")