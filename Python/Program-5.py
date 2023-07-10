set1 = set(input("Set-A:").split())
set2 = set(input("Set-B:").split())
if set1.issubset(set2):
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")
