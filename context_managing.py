# Changing decimal precision 
# or any other context configuration

# don't need to save the old config
# just to restore it later
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)

# use localcontext
from decimal import localcontext
with localcontext(Context(prec=50)):
    print(Decimal(355) / Decimal(113))
# from docs.python.org
with localcontext() as ctx:
    ctx.prec = 42   # Perform a high precision calculation
    s = calculate_something()
s = +s  # Round the final result back to the default precision




# Files

# old way
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
# new way
with open('data.txt') as f:
    data = f.read()


# Locks
import threading

lock = threading.Lock()

# old way
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()
# new way
with lock:
    print('Critical section 1')
    print('Critical section 2')



# Factor-out temporary contexts
# catch exceptions but don't do nothing
import os

# don't do this
try:
    os.remove('somefile.tmp')
except OSError:
    pass

# use contextmanager to create ignored()
# so we can ignore passed exceptions
from contextlib import contextmanager
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
with ignored(OSError):
    os.remove('somefile.tmp')



with open('help.txt','w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

# in python 3.4 we can just import redirect_stdout
# Context manager for temporarily redirecting sys.stdout to another file or file-like object
from contextlib import redirect_stdout
# before that, use contextmanager to create redirect_stdout()
# in both cases, it will send the "print" to the fileobj

from contextlib import contextmanager
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
