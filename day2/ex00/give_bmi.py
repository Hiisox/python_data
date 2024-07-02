def main():
	height = [2.71, 4]
	weight = [165.3, 38.4]
	bmi = give_bmi(height, weight)
	print(bmi, type(bmi))
	print(apply_limit(bmi, 26))


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float] :
	try :
		bmi_list = [(weight[x] / height[x] ** 2) for x in range(len(weight))]
	except:
		print("AssertionError: incorrect list")
		return []
	return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	try :
		bmi_limit_list = [True if x < limit else False for x in bmi]
	except:
		print("AssertionError: incorrect list")
	return bmi_limit_list

if __name__ == "__main__":
	main()