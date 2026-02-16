import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    list_time = s.split()

    if list_time[0].find(':') == -1:
        list_time[0] += ":00"
    if list_time[3].find(':') == -1:
        list_time[3] += ":00"

    check1 = list_time[0].split(':')
    check2 = list_time[3].split(':')
    if int(check1[0]) > 12 or int(check1[0]) < 1 or int(check1[1]) > 59 or int(check1[1]) < 0 or int(check2[0]) > 12 or int(check2[0]) < 1 or int(check2[1]) > 59 or int(check2[1]) < 0:
        return 

    if list_time[1] == "PM":
        tmp = list_time[0].split(':')
        list_time[0] = str(int(tmp[0]) + 12) + ':' + tmp[1]
    if list_time[4] == "PM":
        tmp = list_time[3].split(':')
        list_time[3] = str(int(tmp[0]) + 12) + ':' + tmp[1]

    return list_time[0] + " to " + list_time[3]


if __name__ == "__main__":
    main()