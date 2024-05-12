def checkio(number: int) -> int:
    dobutok=1
    number_str = str(number)
    number_str = number_str.replace('0', '')
    number_str = number_str.replace('', ' ')

    number = [int(num) for num in number_str[1:-1].split()] #Цей рядок я взяв з ChatGPT

    for num in number:
        dobutok = dobutok * num

    return dobutok


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
