# using keywords arguments improves readability
twitter_search('@obama', False, 20, True)
twitter_search('@obama', retweets=False, numtweets=20, popular=True)



# printing tuple is better when using namedtuple()
# because it gives you the keywords
doctest.testmod() 
# (0, 4)
doctest.testmod()
# TestResults(failed=0, attempted=4)
TestRestuls = namedtuple('TestResults', ['failed', 'attempted'])



# this is what is done in other languages
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
# in python, use unpacking
fname, lname, age, email = p


# update multiple state variables
# in other languages we need to use temporary variables
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t
# in python this is better and faster
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


# simultaneous state updates
# don't use tmp variables
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dx = tmp_dy
# use this
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))




