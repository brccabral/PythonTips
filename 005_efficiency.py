
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

# don't join strings with +=
s = names[0]
for name in names[1:]:
    s += ', ' + name
print(s)
# use join function
print(", ".join(names))



# don't use "list" if you are going to del/pop/insert
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
del names[0] # deletes raymond
names.pop(0) # deletes rachel
names.insert(0, 'mark') # insert mark at beggining
print(names)

# use deque()
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])
del names[0]
names.popleft()
names.appendleft('mark')
print(names)
