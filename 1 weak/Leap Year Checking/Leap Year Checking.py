#Leap Year Checking
def is_leap_year(year: int) -> bool:


    year=str(year)

    if len(year)==1 or len(year)==2:
        return False
    if year[2] == '0' and year[3] == '0':
        year = int(year)
        year = year / 400
        year = str(year)
        if year[-2:] == '.0':
            return True
        else:
            return False
    else:
        year=int(year)
        year=year / 4
        year=str(year)
        if year[-2:] == '.0':
            return True
        else:
            return False





print("Example:")
print(is_leap_year(2008))

# These "asserts" are used for self-checking
assert is_leap_year(1608) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
