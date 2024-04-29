def middle(text: str) -> str:
    q=len(text)
    qq=q//2
    aa=qq-1
    if q-qq==qq:
        return text[aa] + text[qq]
    else:
        return text[qq]

print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
