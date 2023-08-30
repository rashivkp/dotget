def dotget(data, name, default=None, first_match=True):
    """
    Access elements from nested list using dot notation
    - Wont provide warning if element not found
    - Wont support multiple arsterics

    first_match: if True, it returns the first match value, else return list of
    matches.

    Eg:
        data = {'a': {'b': [{'c': 1}, {'c': 4}]}}
        dotget(data, "a.b.c=1.c")
        # 1

        dotget(data, "a.b.*.c")
        # [1, 4]
    """
    if type(name) == str:
        name = name.split(".")

    value = default
    name_count = len(name)
    if name_count == 0:
        return data

    if type(data) == dict:
        keys = name[0].split(",")
        if len(keys) > 1:
            value = {k: data.get(k) for k in keys}
        else:
            value = data.get(name[0])
    elif type(data) == list and name[0] == "*":
        return [dotget(item, name[1:], default=default, first_match=first_match) 
                for item in data]
    elif type(data) == list:
        try:
            k, v = name[0].split("=")
        except ValueError:
            return value
        if not first_match:
            return [dotget(item, name[1:], default=default, first_match=first_match) 
                    for item in data if str(item.get(k)) == v]            
        value = next((item for item in data if str(item.get(k)) == v), None)

    if name_count == 1:
        return value or default
    return dotget(value, name[1:], default=default, first_match=first_match)

