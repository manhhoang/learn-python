import copy

# Dictionaries store mappings
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Deep cope dictionary
copy_dic = copy.deepcopy(filled_dict)

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
valid_dict = {(1, 2, 3): [1, 2, 3]}  # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - Dictionary key
# ordering is not guaranteed. Your results might not match this exactly.
list(filled_dict.keys())  # => ["three", "two", "one"]

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict  # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four": 4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
# filled_dict["four"] = 4        #another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
# {'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
# {'a': 1, **{'a': 2}}  # => {'a': 2}

# splat operator
old_dict = {'hello': 'world', 'foo': 'bar'}
new_dict = {**old_dict, 'foo': 'baz'}
