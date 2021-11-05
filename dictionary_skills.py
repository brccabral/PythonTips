# relationships, linking, counting and grouping

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k in d:
    print(k)
print(d)

# use keys() when you want to make changes to the dict
# while the loop is active
# in python3 we need to list() the keys()
for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]
print(d)

# one liner
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
d = {k: d[k] for k in d if not k.startswith('r')}
print(d)


d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
# don't do this
for k in d:
    print(f'{k} --> {d[k]}')
# use items()
for k, v in d.items():
    print(f'{k} --> {v}')
# python3 doesn't have iteritems()
# for k, v in d.iteritems():
#     print(f'{k} --> {v}')


# Create dict from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
d = dict(zip(names, colors))
print(d)
# if you need numbered indexes
d = dict(enumerate(names))
print(d)

# Counting

colors = ['red', 'green', 'red', 'blue', 'green', 'yellow', 'red']

# don't do this
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
# use get() to return a default value if key is not found
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)
# better way = use defaultdict() to set the default value if not found
# the default for int is 0
from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)


# Group

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

# key = group by len() of each word (can be other kind of functions)
# {7: ['raymond', 'matthew', 'melissa', 'charlie'], 6: ['rachel', 'judith'], 5: ['roger', 'betty']}

# don't do this
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)
# use this
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print(d)
# better way
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)


# popitem() is atomic, which can be used when dealing with multiple threads

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
    key, value = d.popitem()
    print(f'{key} --> {value}')
