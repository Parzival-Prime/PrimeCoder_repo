import re


def reverse_only_letters(s: str) -> str:
    s_list = list(s)
    s_rev = s[::-1]
    s_rev_list = list(re.sub(r'[^a-zA-Z]', '', s_rev))
    j = 0
    for i in range(len(s)):
        if s_list[i] in s_rev_list:
            s_list[i] = s_rev_list[j]
            j += 1

    result = ''.join(s_list)
    return result


response = reverse_only_letters('uikkfjg=3&%eyw9389')
print(response)
