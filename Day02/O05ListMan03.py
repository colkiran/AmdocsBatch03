
"""
sort        -   will sort the orginal list
sorted      -   will take a copy of the list and sort it
"""


print("sort".center(40, "-"))
l1 = [7, 10, 5, 1, 9, 3, 8, 2, 4, 6]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

l1 = ['zebra', 7, 'apple', 10, 'yellow', 5, 'blue', 1, 'violet', 9, 'pink', 3, 'red', 8, 'green', 2, 'orange', 4, 'cat', 6, 194, 1423, 27, 241, 2190]

print(f"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(res)

print("-" * 40)
months = ['apr', 'aug', 'dec', 'sep', 'mar', 'jan', 'oct', 'may', 'nov', 'jun', 'feb', 'jul']

print(f"Usorted Months :{months}")

from calendar import month_name
print(list(month_name))
l = []
for month in list(month_name):
    l.append(month[0:3].lower())

def sort_month(mon):
    if mon in l:
        return l.index(mon)

print('-' * 40)
res = sorted(months, key=sort_month)


print(f"res :{res}")

print("reversed".center(40, "-"))

l1 = [7, 10, 5, 1, 9, 3, 8, 2, 4, 6]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")

l2 = l1             # shallow copy = it copies the addres along with data

print(f"l2 Before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("=" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 Before :{l3}")

l4 = l3.copy()

print(f"l4 Before :{l4}")
l4.extend([11, 12, 13, 14])
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("=" * 40)
l5 = [11, 22, 33, 44, [1, 2, 3, 4, 5], 55]
print(f"l5 Before :{l5}")

l6 = l5.copy()
print(f"l6 Before :{l6}")

l6[4].extend([6, 7, 8, 9])
print(f"l6  After :{l6}")
print(f"l5  After :{l5}")

print("=" * 40)
l7 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(F"l7 Before :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)

print(f"l8 Before :{l8}")

l8[4].extend([60, 70, 80])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
