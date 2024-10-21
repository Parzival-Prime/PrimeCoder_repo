def valid_palindrome_2(string: str) -> bool:
    def check(first_string, second_string, k):
        f_stringList = first_string.copy()
        s_stringList = second_string.copy()
        del f_stringList[k]
        del s_stringList[len(s_stringList) - 1 - k]
        return f_stringList == s_stringList

    string_list = list(string)
    reversed_string_list = list(string[::-1])
    for i in range(len(string) - 1):
        print("i: ", i)
        if string_list[i] != reversed_string_list[i]:
            if check(string_list, reversed_string_list, i) or check(reversed_string_list, string_list, i):
                return True
            else:
                return False
    return True


result = valid_palindrome_2("abc")
print(result)
