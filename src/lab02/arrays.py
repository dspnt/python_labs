def min_max(nums: list[float or int]) -> tuple[float or int, float or int]:
    if len(nums) == 0:
        raise ValueError("ValueError")
    mn = min(nums)
    mx = max(nums)
    return(mn,mx)

def unique_sorted(nums: list[float or int]) -> list[float or int]:
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return(nums)

def flatten(mat: list[list or tuple]) -> list:
    a = []
    for i in mat:
        if not isinstance(i, (list, set, tuple)):
            raise TypeError("TypeError")
        for b in i:
            a.append(b)
    return(a)
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))





