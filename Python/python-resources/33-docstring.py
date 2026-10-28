def print_number_info(num):
    """
    Returns info regarding num, whether num is even or odd

    :param int num: Number to be evaluated
    :return str: Returns string which tells whether num is even or odd
    """
    if (num % 2) == 0:
        return "Num is even"
    else:
        return "Num is odd"


print(print_number_info(21))
