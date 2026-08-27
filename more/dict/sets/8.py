#Given a list and a target, determine whether two elements add up to the target using a dictionary.
a = [2, 7, 11, 15]
target = 9
seen = set()
for x in a:
    needed = target - x
    if needed in seen:
        print(True)
        break
    seen.add(x)
else:
    print(False)