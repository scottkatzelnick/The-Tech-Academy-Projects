

import os


def open_file():
    with open('text.txt', 'rt') as f:
        data = f.read()
        print(data)
        f.close()


def write_data():
    data = '\nHello World!'
    with open('text.txt', 'a') as f:
        f.write(data)
        f.close()


if __name__ == '__main__':
    write_data()
    open_file()