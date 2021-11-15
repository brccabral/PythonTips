d = {"a": 1, "b": 2, "c": 3}
# don't loop just to get the keys
for key in d.keys():
    print(key)
# the default is to get the keys
for key in d:
    print(key)

# unless you are going to make changes to original dict
# then, make a copy using list() before the changes
for key in list(d.keys()):
    print(key)
# but even then it is not necessary
for key in list(d):
    print(key)

# don't get the value inside the loop
for key in d:
    val = d[key]
# use items
for key, val in d.items():
    print(val)