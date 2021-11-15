a = [1, 2, 3]
# don't get the len
for i in range(len(a)):
    v = a[i]
    pass
# just loop in the list
for v in a:
    pass

# if you need the index, use enumerate
for i, v in enumerate(a):
    pass

a = [1, 2, 3]
b = [4, 5, 6]
# don't do this
for av, bv in range(len(b)):
    av = a[i]
    bv = b[i]
    pass
# use zip()
for av, bv in zip(a, b):
    pass
# with index
for i, (av, bv) in enumerate(zip(a, b)):
    pass