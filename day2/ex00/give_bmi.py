def check_data(height, weight) -> bool:
    if len(weight) != len(height):
        return False
    for x in range(len(height)):
        if height[x] < 1 or weight[x] < 1:
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if check_data(height, weight) is False:
        print("AssertionError: incorrect list")
        return None
    bmi_list = [(weight[x] / height[x] ** 2) for x in range(len(weight))]
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if bmi is None:
        return None
    bmi_limit_list = [True if x < limit else False for x in bmi]
    return bmi_limit_list
