hrs = int(input("Hour: "))

def convert (hour):
    """
    converts Hours in to seconds (hours * 3600)
    Args: hours(int)
    return: (int value) number of seconds in hours
    """
    seconds = 3600
    result = hour * seconds
    return result

if __name__ == "__main__":
    output = convert(hrs)
    print(f"Hour: {str(hrs)} is equal to {str(output)}")