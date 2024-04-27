def end_zeros_by_Andr(a: int) -> int:
    a = str(a)

    if '0' in a:
        if '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a:

            if a[-1] == '0':
                if a[-2] == '0':
                    if a[-3] == '0':
                        if a[-4] == '0':
                            if a[-5] == '0':
                                if a[-6] == '0':
                                    return 6
                                else:
                                    return 5
                            else:
                                return 4
                        else:
                            return 3
                    else:
                        return 2
                else:
                    return 1
            else:
                return 0
        else:
            return len(a)
    else:
        return 0


def end_zeros(a: int) -> int:
    str_a = str(a)
    reverse_a = str_a[::-1]
    count = 0
    for symbol in reverse_a:
        if symbol == '0':
            count = count + 1
        else:
            break
    return count


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
