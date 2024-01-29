def total(arr):
    def sqrt(n):
        isprime = True
        for x in range(2, int(n ** 0.5) + 1):
            if i % x == 0:
                isprime = False
                break
        return isprime
    sum = 0
    for i in range(2, len(arr)):
        if sqrt(i):
            sum += arr[i]
    return sum

print(total([1,2,3,4,5,6])) # 13
