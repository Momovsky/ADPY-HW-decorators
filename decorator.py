from datetime import datetime
import os


def logger(path):
    file_path = os.path.join(path, 'log.txt')

    def _logger(old_function):
        statistics = {}

        def new_func(*args, **kwargs):
            nonlocal statistics
            nonlocal file_path
            statistics['starting_time'] = datetime.now().ctime()
            result = old_function(*args, **kwargs)
            statistics['name'] = old_function.__name__
            statistics['args'] = args
            statistics['result'] = result
            with open(file_path, 'w', encoding='utf-8') as file:
                print(statistics, file=file)
            return result

        return new_func
    return _logger

@logger('/Users/igorkirillov/Desktop')
def foo(a, b):
    return a * b


foo(121, 231)
