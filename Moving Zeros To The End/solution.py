def move_zeros(lst):
    With_Zero = []
    Without_Zero = []
    for i in lst:
        if i == 0:
            With_Zero.append(i)
        else:
            Without_Zero.append(i)
    Without_Zero.extend(With_Zero)
    return Without_Zero
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
