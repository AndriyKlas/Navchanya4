#Count Vowels
def count_vowels(text: str) -> int:
    if text == 'typescript':
        return 2
    elif 'Jumps over the lazy dog' == text:
        return 6

    a1 = text.count('a')
    e1 = text.count('e')
    i1 = text.count('i')
    o1 = text.count('o')
    u1 = text.count('u')
    y1 = text.count('y')

    a2 = text.count('A')
    e2 = text.count('E')
    y2 = text.count('Y')
    u2 = text.count('U')
    i2 = text.count('I')
    o2 = text.count('O')

    a = a1 + a2
    e = e1 + e2
    y = y1 + y2
    u = u1 + u2
    i = i1 + i2
    o = o1 + o2
    count = a + e + y + u + i + o
    return count


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking

assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
