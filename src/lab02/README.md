# Лабораторная работа №1

## Задание 1
## min_max
```python
def min_max(nums: list[float or int]) -> tuple[float or int, float or int]:
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    if len(nums) == 0:
        raise ValueError("ValueError")
    mn = min(nums)
    mx = max(nums)
    return(mn,mx)
```
![47](/images/lab2/arrays1.png)
## unique_sorted
```python 
def unique_sorted(nums: list[float or int]) -> list[float or int]:
    if not isinstance(nums, list):
        raise TypeError("TypeError")
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return(nums)
```
![47](/images/lab1/arrays2.png)
## Задание flatten
```python
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
```
![47](/images/lab1/arrays3.png)

# Задание 2
## transpose
```python
def transpose(mat: list[list[float or int]]) -> list[list]:
    if len(mat) == 0:
        return []
    if len(mat) != 0:
        ln = len(mat[0])
    for i in mat:
        if len(i) != ln:
            raise TypeError('"ValueError"')
    if not isinstance(mat, list):
        raise TypeError('TypeError')
    a = []
    sr = len(mat)
    st = len(mat[0])
    for i in range(st):
        b = []
        for j in range(sr):
            b.append(mat[j][i])
        a.append(b)
    return a
```
![47](/images/lab1/matrix1.png)
## row_sums
```python
def row_sums(mat: list[list[float or int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if len(mat) != 0:
        ln = len(mat[0])
    for i in mat:
        if len(i) != ln:
            raise TypeError('"ValueError"')
    if not isinstance(mat, list):
        raise TypeError('TypeError')
    a = []
    for i in mat:
        sm = 0
        for j in i:
            sm += j
        a.append(sm)
    return(a)
```
![47](/images/lab1/matrix2.png)
## col_sums
```python
def col_sums(mat: list[list[float or int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if len(mat) != 0:
        ln = len(mat[0])
    for i in mat:
        if len(i) != ln:
            raise TypeError('"ValueError"')
    if not isinstance(mat, list):
        raise TypeError('TypeError')
    a = []
    for i in range(len(mat[0])):
        b = 0
        for j in range(len(mat)):
            b += mat[j][i]
        a.append(b)
    return(a)
```
![47](/images/lab1/matrix3.png)

# Задание 3
```python
def format_record(rec: tuple[str, str, float]):
    fio,group,gpa = rec
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError('ValueError')
    if not isinstance(group, str) or not group.strip():
        raise ValueError('ValueError')
    if not isinstance(gpa, (int, float)):
        raise ValueError('ValueError')
    initials = ""
    parts = fio.strip().split()
    fam = parts[0]
    fam = fam.title()
    for a in parts[1:]:
        initials += a[0].upper() + "."
    if not initials:
        initials = ""
    form_gpa=f"{gpa:.2f}"
    return f"{fam} {initials}, гр. {group}, GPA {form_gpa}"
```
![47](/images/lab1/tuples.png)