from termcolor import colored
import datetime


def print_with_color(text, color='red'):
    """
    Print text with color
    :param text:
    :param color:
    :return:
    """
    print(colored(text, color))


def logger(error, traceback='', file=None):
    """
    write to log
    :param error:
    :param traceback:
    :param file:
    :return:
    """
    if file is None:
        file = 'website/storage/logs/flask-' + str(datetime.date.today()) + '.log'
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, 'a') as fo:
        fo.write("[" + date + "] " + error + "\n" + traceback + "\n")
