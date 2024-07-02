
def slice_me(family: list, start: int, end: int) -> list:
	size = -1
	height = 0
	for x in family :
		if type(x) != list :
			print("AssertionError: only list are allowed")
			return None
		if size == -1 :
			size = len(x)
		elif size != len(x) :
			print("AssertionError: list should have the same size")
			return None
		height += 1
	print(f"my shape is : ({height}, {size})")
	i = slice(start, end)
	height = 0
	size = -1
	for x in family[i] :
		if size == -1 :
			size = len(x)
		height += 1
	print(f"my new shape is : ({height}, {size})")
	return family[i]

family = [1]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))