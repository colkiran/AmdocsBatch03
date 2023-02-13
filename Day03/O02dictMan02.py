

print("keys".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'country': 'Argentina', 'ballondor': 7}

k = player.keys()
print(f"k :{k}")

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'country': 'Argentina', 'ballondor': 7}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(v)

print("get".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'ballondor': 7}
print(f"player :{player}")

print(f"Name    :{player.get('name',  'Invaid key, Please enter a valid one')}")
print(f"Country :{player.get('country', 'Invaid key, Please enter a valid one')}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")
res = dict.fromkeys(cities)
print(f"res :{res}")

res1 = dict.fromkeys(cities, 24)
print(f"res1 :{res1}")

print("setdefault".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'ballondor': 7}
print(f"player :{player}")

print("-" * 40)
player.setdefault('goals', 365)
player.setdefault('country', 'Argentina')
player.setdefault('club', 'FCB')
print(f"player :{player}")

print("pop".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'ballondor': 7, 'country': 'Argentina'}
print(f"player :{player}")

print("-" * 40)
res= player.pop('age')
print(f"res :{res}")

res= player.pop('club')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'ballondor': 7, 'country': 'Argentina'}
print(f"player :{player}")

print("-" * 40)
res = player.popitem()
print(res)

res = player.popitem()
print(res)

print(f"player :{player}")
