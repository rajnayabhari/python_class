# Dictionary keys has a restriction that they must be immutable data-type.
# There is no such restriction in dictionary values

d = {"name": "john", "age": 25}  # valid
d = {1: "Hello", 2: "world"}  # valid
e = {2.45: 2, 2.3: 3}  # valid
d = {(1, 2): "hello", (3, 2): "world"}  # valid
e = {[1, 2]: 1, [3, 4]: 2}  # invalid
f = {([1, 2]): 2}  # invalid
