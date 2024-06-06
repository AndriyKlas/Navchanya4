def is_majority(items: list[bool]) -> bool:
    true_num=0
    false_num=0
    index=0

    for major in items:
        if items[index]==True:
            index=index+1
            true_num=true_num+1
        elif items[index]==False:
            index=index+1
            false_num=false_num+1
        else:
            break
    if true_num>false_num:
        return True
    elif true_num<false_num:
        return False
    elif true_num==false_num:
        return False
    elif items=='':
        return False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
