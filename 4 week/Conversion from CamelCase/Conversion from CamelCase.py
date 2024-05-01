def from_camel_case(name: str) -> str:
    index = 0
    for letter in name:
        if name[index] != name[index].upper():
            index = index + 1
        elif name[index] == name[index].upper():
            name = name.replace(name[index], f'_{name[index].lower()}')
            index = index + 1

        else:
            break
    name = name[1:]
    return name


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
