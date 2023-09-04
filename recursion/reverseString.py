def reverseString(str):
    if not str:
        return ""
    return reverseString(str[1:]) + str[0]


a = "hello"
print(reverseString(a))
