
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)
# continue, break, else

for i in range(1, 25):
    # if i > 20:
    #     break           # break the iteration
    if i % 2 == 1:
        continue        # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted the iteration......")