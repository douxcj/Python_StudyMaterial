def uni_char(s):
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for key in d:
        if d[key] != 1:
            return False
    return True


def use_set(s):
    char_set = set(s)
    return len(s) == len(char_set)


def use_set2(s):
    char_set = set()
    for char in s:
        if char not in char_set:
            char_set.add(char)
        else:
            return False
    return True

if __name__ == '__main__':
    print(use_set2('ahdig'))