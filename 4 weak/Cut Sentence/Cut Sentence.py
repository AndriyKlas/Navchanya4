def cut_sentence(line: str, length: int) -> str:
    len_line = len(line)
    length_1 = length
    result = line[:length_1]
    reverse_result = result[::-1]
    skoroch_line = line[length:]
    if len_line <= length:
        return line

    elif skoroch_line[0]==' ':
            return result + '...'


    elif result[-1] == ' ':
        line=str(line[:length_1])
        len_line=len(line)
        line=line[:len_line-1]
        return line +'...'
    else:
        if line[length_1-1] == ' ':
            return line[:length_1] + '...'
        else:
            for neprobil in reverse_result:
                if neprobil != ' ':
                    length_1 = length_1 - 1
                else:
                    break
            line=str(line[:length_1])
            len_line=len(line)
            line=line[:len_line-1]

            return line + '...'


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
assert cut_sentence('Hi my name is Alex', 10) == 'Hi my name...'
assert cut_sentence('Hi my name is Alex', 11) == 'Hi my name...'

print("The mission is done! Click 'Check Solution' to earn rewards!")
