
"""
items is a combination of keys and values function
k, v = items
"""

emp = {
    'emp1': {'name': 'Mike', 'age': 35, 'dept': 'MKT', 'desig': 'BDM', 'loc': 'Delhi', 'exp': '8 yrs' },
    'emp2': {'name': 'Gracy', 'age': 32, 'dept': 'IT', 'desig': 'TL', 'loc': 'Bangalore', 'exp': '6 yrs' },
    'emp3': {'name': 'Borris', 'age': 29, 'dept': 'Finance', 'desig': 'Executive', 'loc': 'Mumbai', 'exp': '4 yrs' }
}

print(f"emp :{emp}")

print("\n", "-" * 40, "\n")

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("\n", "-" * 40, "\n")

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("Update".center(40,  "-"))

emp1 =  {'name': 'Mike', 'age': 35, 'dept': 'MKT', 'desig': 'BDM', 'loc': 'Delhi' }
emp2 =  {'name': 'Gracy', 'age': 32, 'dept': 'IT', 'desig': 'TL', 'exp': '6 yrs' }

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)       # same keys values are directly copied into it

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("clear".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 35, 'dept': 'MKT', 'desig': 'BDM', 'loc': 'Delhi', 'exp': '8 yrs'}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")

print("copy".center(40, "-"))
emp1 =  {'name': 'Mike', 'age': 35, 'dept': 'MKT', 'desig': 'BDM', 'loc': 'Delhi' }
print(f"emp1 Before :{emp1}")

emp2 = emp1                # shallow copy - copies the data along with address

print(f"emp2 Before :{emp2}")

print("-" * 40)
emp2['sal'] = 45000
emp2['exp'] = '10 yrs'

print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("\n", "-" * 40, "\n")
emp3 = {'name': 'Gracy', 'age': 32, 'dept': 'IT', 'desig': 'TL', 'exp': '6 yrs' }
print(f"emp3 Before :{emp3}")

emp4 = emp3.copy()

print(f"emp4 Before :{emp4}")
emp4['sal'] = 45000
emp4['exp'] = '10 yrs'

print("-" * 30)
print(f"emp4 After :{emp4}")
print(f"emp3 After :{emp3}")

print("\n", "-" * 40, "\n")

emp5 = {'name': 'Borris', 'age': 29, 'dept': 'Finance', 'desig': {'hp': 'trainee', 'IBM': 'Executive'}, 'loc': ['chennai', 'Mumbai'], 'exp': '4 yrs' }

print(f"emp5 Before : {emp5}")

emp6 = emp5.copy()

print(f"emp6 Before :{emp6}")

print("-" * 40)
emp6['desig']['ABB'] = 'Sr Executive'
emp6['loc'].append('Hyderabad')

print(f"emp6 After :{emp6}")
print(f"emp5 After :{emp5}")

print("\n", "-" * 40, "\n")

emp7 = {'name': 'Borris', 'age': 29, 'dept': 'Finance', 'desig': {'hp': 'trainee', 'IBM': 'Executive'}, 'loc': ['chennai', 'Mumbai'], 'exp': '4 yrs' }

print(f"emp7 Before :{emp7}")
from copy import deepcopy

emp8 = deepcopy(emp7)
print(f"emp8 Before :{emp8}")

print("-" * 40)
emp8['desig']['ABB'] = 'Sr Executive'
emp8['loc'].append('Hyderabad')

print(f"emp8 After :{emp8}")
print(f"emp7 After :{emp7}")