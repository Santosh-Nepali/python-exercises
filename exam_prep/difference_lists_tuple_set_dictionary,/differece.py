# List — ordered, mutable, allows duplicates
my_list = [1, 2, 2, 3]
my_list.append(4)
print(my_list)   # [1, 2, 2, 3, 4]

# Tuple — ordered, immutable, allows duplicates
my_tuple = (1, 2, 2, 3)
# my_tuple.append(4)  # would raise AttributeError

# Set — unordered, mutable, NO duplicates
my_set = {1, 2, 2, 3}
print(my_set)   # {1, 2, 3}  <- duplicate automatically removed

# Dictionary — ordered (3.7+), mutable, unique keys
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
print(my_dict)   # {'a': 1, 'b': 2, 'c': 3}