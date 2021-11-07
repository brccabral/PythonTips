# don't need to store data in a saved dict
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# use cache when the return value is the same
# for the same parameter
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

# in python 3.9 you can import it
# from functools import cache
# older python
from functools import wraps
def cache(func):
    saved = {}
    # without wraps() the DocString will be the 
    # one from the decorator "cache"
    @wraps(func) 
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc
