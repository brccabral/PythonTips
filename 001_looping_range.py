
for i in [0,1,2,3,4,5]:
    print(i**2)

for i in range(6):
    print(i**2)

# Python 3 doesn't have xrange(), it is range() itself
# to get the list in python3, list(range())
# for i in xrange(6):
#     print(i**2)

colors = ['red', 'green', 'blue', 'yellow']

# don't do this
for i in range(len(colors)):
    print(colors[i])

# do this, get the value
for color in colors:
    print(color)


# don't loop backwards like this
for i in range(len(colors)-1,-1,-1):
    print(colors[i])

# use reversed
for color in reversed(colors):
    print(color)


# don't do this
for i in range(len(colors)):
    print(f'{i} --> {colors[i]}')

# use enumerate()
for i, color in enumerate(colors):
    print(f'{i} --> {color}')

# Looping over two collections

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# don't do this
n = min(len(names), len(colors))
for i in range(n):
    print(f'{names[i]} --> {colors[i]}')

# use zip()
for name, color in zip(names, colors):
    print(f'{name} --> {color}')

# Python 3 doesn't have izip(), it is zip() itself
# for name, color in izip(names, colors):
#     print(f'{name} --> {color}')


for color in sorted(colors):
    print(color)
for color in sorted(colors, reverse=True):
    print(color)

# Custom sort order

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0
from functools import cmp_to_key
# this is slower because it does two len() comparisons
print(sorted(colors, key=cmp_to_key(compare_length)))
# use this, only one len()
print(sorted(colors, key=len))

# Call a function until a sentinel value (if something: break)

from functools import partial
with open("README.md", "r") as f:
    blocks = []
    while True:
        block = f.read(32)
        if block == '':
            break
        blocks.append(block)
    print(blocks)
    
    # the tip here is to use iter(), because the result can be used
    # in many other iterable functions like min(), max(), enumerate()
    # iter() first argument needs a function with no arguments
    # so, we can't put f.read() directly, we use partial() to 
    # simulate the behavior of f.read()
    f.seek(0)
    blocks = []
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)
    print(blocks)

# Distinguishing multiple exit points in loops

def find(seq, target):
    """If found value, return index, return -1 if not found

    Args:
        seq (iter): iteractable
        target (Any): search value

    Returns:
        int: index or -1
    """
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

print(find(colors, 'red'))
print(find(colors, 'black'))

# use "else" to handle a short stop in for
def find_better(seq, target):
    """If found value, return index, return -1 if not found

    Args:
        seq (iter): iteractable
        target (Any): search value

    Returns:
        int: index or -1
    """
    found = False
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        # execute if a break is called
        return -1
    return i

print(find_better(colors, 'red'))
print(find_better(colors, 'black'))