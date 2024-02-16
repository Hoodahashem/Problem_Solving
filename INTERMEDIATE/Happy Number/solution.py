def isHappy(n):
  """
  :type n: int
  :rtype: bool
  """
  seen = []
  string = str(n)
  sum = 0
  while sum != 1:
    sum = 0
    for i in string:
      x = int(i)
      sum += x ** 2
    if sum in seen:
      return False
    seen.append(sum)
    string = str(sum)
  return True

print(isHappy(19)) # True
print(isHappy(2)) # False
print(isHappy(7)) # True
print(isHappy(1111111)) # False
