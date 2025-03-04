# Programmer: Mason Colacicco
# Date: March
# Program: Speed Comparison

import datetime

def main():
    events = []
    ol_2016s = []
    ol_1924s = []
    try:
        while True:
            event = input("Input event name: ")
            hr_2016 = int(input("2016 event time of hours:  "))
            min_2016 = int(input("2016 event time of minutes:  "))
            sec_2016 = int(input("2016 event time of seconds:  "))
            mil_2016 = int(input("2016 event time of milliseconds:  "))
            hr_1924 = int(input("1924 event time of hours:  "))
            min_1924 = int(input("1924 event time of minutes:  "))
            sec_1924 = int(input("1924 event time of seconds:  "))
            mil_1924 = int(input("1924 event time of milliseconds:  "))
            if event == 'q':
                break
            else:
                break
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()