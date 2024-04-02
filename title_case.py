def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    if str1 == str2:
        if threshold==0:
            return True
        else:
            return False
    elif len(str1) == len(str2) and len(str1)==6:
        if str1[0] == str2[0]:
            if str1[1] == str2[1]:
                if str1[2] == str2[2]:
                    if str1[3] == str2[3]:
                        if str1[4] == str2[4]:
                            if str1[5] == str2[5]:
                                if threshold == 0:
                                    return True
                                else:
                                    return False
                            elif threshold == 1:
                                    return True
                            else:
                                return False
                        elif str1[5] == str2[5]:
                            if threshold == 1:
                                return True
                            else:
                                return False
                        elif threshold == 2:
                            return True
                        else:
                            return False
                    elif str1[4] == str2[4]:
                        if str1[5] == str2[5]:
                            if threshold == 1:
                                return True
                            else:
                                return False
                        elif threshold == 2:
                            return True
                        else:
                            return False
                    elif str1[5] == str2[5]:
                        if threshold == 2:
                            return True
                        else:
                            return False
                    elif threshold == 3:
                        return True
                    else:
                        return False
                elif str1[3] == str2[3]:
                    if str1[4] == str2[4]:
                        if str1[5] == str2[5]:
                            if threshold == 1:
                                return True
                            else:
                                return False
                        elif threshold == 2:
                            return True
                        else:
                            return False
                    elif str1[5] == str2[5]:
                        if threshold == 2:
                            return True
                        else:
                            return False
                    elif threshold == 3:
                        return True
                    else:
                        return False
                elif str1[4] == str2[4]:
                    if str1[5] == str2[5]:
                        if threshold == 1:
                            return True
                        else:
                            return False
                    elif threshold == 2:
                        return True
                    else:
                        return False
                elif str1[5] == str2[5]:
                    if threshold == 2:
                        return True
                    else:
                        return False
                elif threshold == 3:
                    return True
                else:
                    return False





    return str1[0]

print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
