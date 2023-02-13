

d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Micheal'), ('age', 34), ('desig', 'MGR'), ('sal', 95000), ('dept', 'finance')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='messi', age=36, goals=350, club='PSG', country='Argentina')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Messi', 'age': 36, 'goals': 350, 'club': 'PSG', 'country': 'Argentina'}
print(f"player :{player}")
print(type(player))

# extract data
print("-" * 40)
print(f"Name :{player['name']}")
print(f"Age  :{player['age']}")
print(f"Club :{player['club']}")

# iterate
print("-" * 40)
for i in player:                # accessing the keys of the dictionary
    print(i, "=>", player[i])

# modify
print("-" * 40)
player['name'] = 'Lionel Messi'
player['age'] = 35
player['ballondor'] = 7

print(f"player :{player}")

# delete
print("-" * 40)
del player['age']
del player['club']

print(f"player :{player}")

print("-" * 40)
print(dir(player))
