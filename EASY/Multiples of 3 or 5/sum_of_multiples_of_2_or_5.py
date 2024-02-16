def solution(number):
    lst = []
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
    for x in lst:
        sum += x
    return sum

# Simple_test
print(solution(4)) # the output should be => 3
