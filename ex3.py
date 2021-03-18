"""
@project: WeThinkCode (Bootcamp)
@Author: Sello sydney Mafikeng
@email: tebogomafikeng@gmail.com
@file: ex3.py
"""

spam1 , spam2 , spam3 = input("first: ") , input("second: ") , input("Third: ")
spam = [spam1 , spam2 , spam3]

def separate (spamlist):
    """
    separate list items with a comma and space
    Args: (list spamlist)
    Return: list separated by comma and space
    """
    result = ', '.join(spamlist)    #takes items in a iterable and joins the into one string
    return result

if __name__ == "__main__":
    output = separate(spam)
    print(output)
