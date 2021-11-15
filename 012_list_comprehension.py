# don't do this
squares = {}
for i in range(10):
    squares[i] = i * i
# use list comprehension
squares = {i: i * i for i in range(10)}


dict_comp = {i: i * i for i in range(10)}
list_comp = [x*x for x in range(10)]
set_comp = {i%3 for i in range(10)}
generator_comp = (2*x+5 for x in range(10))


# don't use it nested in each other
def always_using_comprehensions(a, b, n):
    """matrix product of a, b of length n x n"""
    return [
        sum(a[n*i+k]*b[n*k+j] for k in range(n)) # it throws error, but is just an example
        for i in range(n)
        for j in range(n)
    ]
# it is better "for loops" to make it easier to read
def readibility_sometimes_is_better(a, b, n):
    """matrix product of a, b of length n x n"""
    c = []
    for i in range(n):
        for j in range(n):
            ij_entry = sum(a[n*i+k]*b[n*k+j] for k in range(n)) # it throws error, but is just an example
            c.append(ij_entry)
    return c