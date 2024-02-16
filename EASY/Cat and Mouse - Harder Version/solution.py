def cat_mouse(x,j):
    Cat = "C"
    Dog = "D"
    Mouse = "m"

    if Cat not in x or Mouse not in x or Dog not in x:
        return "boring without all three"

    Cat_Pos = x.index(Cat)
    Mouse_Pos = x.index(Mouse)
    distance = abs(Cat_Pos - Mouse_Pos)

    if distance > j:
        return "Escaped!"
    elif distance <= j and Dog in x[Cat_Pos:Mouse_Pos+1] or Dog in x[Mouse_Pos:Cat_Pos+1]:
        return "Protected!"
    else:
        return "Caught!"


print(cat_mouse('m....D.........C......', 18)) # "Protected!"
