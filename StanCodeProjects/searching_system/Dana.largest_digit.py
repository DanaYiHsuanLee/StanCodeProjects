"""
File: largest_digit.py
Name: Dana
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int, return a largest digit among n
	"""
	return find_largest_digit_helper(n, 0, 0)


def find_largest_digit_helper(n, nn, maximum):
	"""
	:param n: int
	:param nn: int, the power as the digit of n
	:param: int, maximum, a largest digit among n
	:return: int, maximum
	"""
	if n < 0:
		n *= -1
	num = int(n/(10**nn))-(int(n/(10**(nn+1)))*10)
	if 0 < n/(10**nn) < 1:
		return maximum
	else:
		if num > maximum:
			maximum = num
		return find_largest_digit_helper(n, nn+1, maximum)


if __name__ == '__main__':
	main()
