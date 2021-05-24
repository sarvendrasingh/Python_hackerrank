# program to find 256th day of any year
# leap year is based on julian calendar upto 1917, ongregorian calender from 1919
# and transition period was 1918 when 14 Feb was 32nd day of year. i.e. 14 Feb came just after 31st Jan in 1918

def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            return '12.09.' + str(year)
        return '13.09.' + str(year)
    elif year > 1918:
        if year % 4 == 0 and year % 100 != 0:
            return '12.09.' + str(year)
        elif year % 400 == 0:
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
    else:
        return '26.09.' + str(year)


if __name__ == '__main__':
    year = int(input("Enter year to find its 256th day: ").strip())
    result = dayOfProgrammer(year)
    print(result + '\n')


