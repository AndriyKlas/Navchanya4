def middle(text: str) -> str:
    q=len(text)
    qq=q//2
    aa=qq-1
    if q-qq==qq:
        return text[aa] + text[qq]
    else:
        return text[qq]


def middle_by_Maks(text):
    length_of_text = len(text)
    middle_index = int(length_of_text / 2)  # ~ length_of_text // 2
    if length_of_text % 2 == 1:
        return text[middle_index]
    else:
        return text[middle_index - 1] + text[middle_index]


print("Example:")
print(middle("test"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
