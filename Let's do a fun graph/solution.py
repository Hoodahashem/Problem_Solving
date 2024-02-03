def graph(arr):
    # making space
    def Make_Space(arr):
        str = ''
        for i in reversed(range(max(arr)+1)):
            for x in range((6 * len(arr)) + 1):
                str += "."
            if i == max(arr):
                str += f" ^ {i}\n"
            else:
                str += f" | {i}\n"
        return str
    str = Make_Space(arr)
    lst = []
    newstr = ''
    for i in str:
        newstr += i
        try:
            int(i)
            lst.append(newstr)
            newstr = ''
        except:
            pass


graph([1, 3, 5, 4, 1])
