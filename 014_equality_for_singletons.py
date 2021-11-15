x = None

# wrong
if x == None:
    pass
if x == True:
    pass
if x == False:
    pass

# correct
if x is None:
    pass
if x is True:
    pass
if x is False:
    pass