def append_wrong(n, l=[]):
    l.append(n)
    return l

l1 = append_wrong(0) # return [0]
l2 = append_wrong(1) # return [0,1], not just [1]

def append_correct(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l

l1 = append_correct(0) # return [0]
l2 = append_correct(1) # return [1] as expected
