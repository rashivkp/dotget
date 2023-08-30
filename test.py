from utils import dotget

data = {'a': {'b': [{'c': 1, "d": 4, "f": 12}, {'c': 4, "d": 4}]}, 'e': [1, 2, 3]}

assert dotget(data, "a.b.c=1.d") == next(filter(lambda x: x.get("c") == 1, data.get("a", {}).get("b", {})), {}).get("d")
# 4

assert dotget(data, "a.b.*.c") == [el.get("c") for el in data.get("a", {}).get("b", {})]
# [1, 4]

assert dotget(data, "a.b.*") == data.get("a", {}).get("b", {})
# [{'c': 1, "d": 4}, {'c': 4, "d": 4}]

assert dotget(data, "a.b.d=4.c", first_match=False) == [el.get("c") for el in filter(lambda x: x.get("d") == 4, data.get("a", {}).get("b", {}))]
# [1, 4]

assert dotget(data, "a.b.c=1.c,d") == next(iter([ {"c": el.get("c"), "d": el.get("d")} for el in filter(lambda x: x.get("c") == 1, data.get("a", {}).get("b", {}))]), None)
# {'c': 1, 'd': 4}

assert dotget(data, "a.b.c=1") == next(filter(lambda x: x.get("c") == 1, data.get("a", {}).get("b", {})), None)
# {'c' 1, 'd': 4, 'f': 12}

assert dotget(data, "a.b.c=1", first_match=False) == list(filter(lambda x: x.get("c") == 1, data.get("a", {}).get("b", {})))
# [{'c': 1, 'd': 4, 'f': 12}]

assert dotget(data, "a.b.d=4", first_match=False) == list(filter(lambda x: x.get("d") == 4, data.get("a", {}).get("b", {})))
# [{'c': 1, 'd': 4}, {'c': 4, "d": 4}]

assert dotget(data, "a.b.*.t", default=5) == [el.get("t", 5) for el in data.get("a", {}).get("b", {})]
# [5, 5]

assert dotget(data, "a.b.c=1.t", default=5) == next(filter(lambda x: x.get("c") == 1, data.get("a", {}).get("b", {})), {}).get("t", 5)
# 5

second_data = [{'c': 1, "d": 4, "f": 12}, {'c': 4, "d": 4}]
assert dotget(data, "c=1.f", default=5) == next(filter(lambda x: x.get("c") == 1, second_data), {}).get("f", 5)
# 12
