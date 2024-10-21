import re


def reverse_vowels(s: str):
    s_list = list(s)
    s_vowels = re.sub(r'[^aeiouAEIOU]', '', s)
    s_vowels = list(s_vowels[::-1])
    # print(s_vowels)
    j = 0
    for i in range(len(s)):
        if s_list[i] in s_vowels:
            # print(s_list[i])
            s_list[i] = s_vowels[j]
            # print(s_list[i])
            j += 1

    result = ''.join(s_list)
    print(result)


reverse_vowels('IceCream')
