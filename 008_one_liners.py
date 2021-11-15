# what goes in one line is what you can 
# express in a single english sentence


# old way
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print(sum(result))
# good way
print(sum([i**2 for i in range(10)]))
# better way, doesn't create the i**2 list
print(sum(i**2 for i in range(10)))

