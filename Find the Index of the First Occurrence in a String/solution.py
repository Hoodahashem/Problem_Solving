'''
in this problem, i didn't know that the index() function in python
can be used to find the first occurence of a substring so i used it to find the first
occurence of a character
'''
# my solution
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    idx = haystack.index(needle[0])
    for i in range(idx, len(haystack)):
        x = i + len(needle)
        if needle == haystack[i:x]:
            print (i)
        print(haystack[i:x])
    print (-1)

# the best solution that you can use this
# def strStr(self, haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     try:
#         idx = haystack.index(needle)
#         return idx
#     except:
#         return -1

print(strStr(0, "hello", "ll")) # 2
print(strStr(0, "aaaaa", "bba")) # -1
print(strStr(0, "a", "a")) # 0
print(strStr(0, "mississippi", "issip")) # 4
print(strStr(0, "mississippi", "issipi")) # -1
print(strStr(0, "mississippi", "issi")) # 1
