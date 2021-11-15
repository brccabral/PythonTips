# use ChainMap to merge many dictionaries

import argparse
import os

# get the defaults, overwrite with enviroment variables
# and then overwrite them with user inputs

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='User')
parser.add_argument('-c', '--color', help='Color')
namespace = parser.parse_args() # in the video this returns empty
command_line_args = {k:v for k, v in 
                        vars(namespace).items() if v}

# don't do this, it does a lot of copying
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
# print(d)
print(d['user'])

# use ChainMap
from collections import ChainMap
d = ChainMap(command_line_args, os.environ, defaults)
# print(d)
print(d['user'])

# ChainMap creates a collection of dict
# it gets the requested value from the first dict on the collection
# if not found, go to the next dict