x = None

# nothing wrong, but not good
if bool(x):
    pass
if len(x) != 0:
    pass

# better
if x:
    pass