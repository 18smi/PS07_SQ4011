import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    num_list = ip.split('.')
    if len(num_list) > 4:
        return False

    for i in num_list:
        if float(i) > 255 or float(i) < 0:
            return False
    return True




if __name__ == "__main__":
    main()