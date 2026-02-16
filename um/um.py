import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    eddeted_string = ' ' + s.replace(',', '').replace('.', '').replace('!', '').replace('?', '') + ' '
    return eddeted_string.lower().count(" um ")




if __name__ == "__main__":
    main()