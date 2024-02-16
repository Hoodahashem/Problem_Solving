def str_count(strng, letter):
	count = 0
	for i in strng:
		if i == letter:
			count += 1
	return count

print(str_count('Hello', 'l')) # 2
print(str_count('Hello', 'e')) # 1
print(str_count('Hello', 'X')) # 0
