#Builtin Modules
import os
print("Current Directory:", os.getcwd())
if not os.path.exists("example_folder"):
    os.mkdir("example_folder")


import sys
print("Python Version:", sys.version)

import platform
print(platform.system(), platform.release(),
platform.processor())

import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)
parsed = json.loads(json_str)
print(parsed["name"])

import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.sin(math.pi / 2))

import random
print(random.randint(1, 100))
print(random.choice(['apple', 'banana', 'cherry']))

from collections import Counter, defaultdict
data = ['a', 'b', 'a', 'c']
counter = Counter(data)
print(counter)
dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])


import itertools
print(list(itertools.combinations('ABCD', 2)))