def checkio(array: list[int]) -> int:
    index=0
    number=0
    if len(array) == 0:
        return 0
    elif len(array) <= 2 :
        return array[0]*array[-1]
    for checkio in array:
        if len(array)-1 >= index:
            number=number+array[index]
            index=index+2
        else:
            break
    return number*array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([6,6]) == 36
assert checkio([6]) == 36
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
