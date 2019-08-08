from termcolor import colored


def print_with_color(text, color='red'):
    """
    Print text with color
    :param text:
    :param color:
    :return:
    """
    print(colored(text, color))
