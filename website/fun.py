from termcolor import colored
import datetime
import traceback


def print_with_color(text, color='red'):
    """
    Print text with color
    :param text:
    :param color:
    :return:
    """
    print(colored(text, color))


def logger(error, if_trace=True, file=None):
    """
    write to log
    :param error:
    :param if_trace:
    :param file:
    :return:
    """
    if file is None:
        file = 'website/storage/logs/flask-' + str(datetime.date.today()) + '.log'
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, 'a') as fo:
        text = "[" + date + "] " + error + "\n"
        if if_trace is True:
            text += traceback.format_exc() + "\n"
        fo.write(text)
