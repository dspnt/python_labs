def min_max(nums: list[float or int]) -> tuple[float or int, float or int]:
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    if len(nums) == 0:
        raise ValueError("ValueError")
    mn = min(nums)
    mx = max(nums)
    return(mn,mx)

def unique_sorted(nums: list[float or int]) -> list[float or int]:
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return(nums)

def flatten(mat: list[list or tuple]) -> list:
    a = []
    if not isinstance(mat, list):
        raise TypeError("TypeError")
    for i in mat:
        if not isinstance(i, (list, set, tuple)):
            raise TypeError("TypeError")
        for b in i:
            a.append(b)
    return(a)






