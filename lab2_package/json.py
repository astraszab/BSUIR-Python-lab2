def dumps(obj):
    """Convert an object to a json string.
    """
    if isinstance(obj, bool):
        if obj:
            return 'true'
        else:
            return 'false'
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return f'"{obj}"'
    elif obj is None:
        return 'null'
    elif isinstance(obj, dict):
        res = '{'
        empty = True
        for key, value in obj.items():
            if not empty:
                res += ', '
            if isinstance(key, str):
                res += f'"{key}": '
            elif isinstance(key, (bool, int, float)) or key is None:
                res += f'"{dumps(key)}": '
            else:
                raise TypeError('Keys must be str, int, float, bool or None, '
                                f'not {type(key).__name__}.')
            res += dumps(value)
            empty = False
        res += '}'
        return res
    elif isinstance(obj, (list, tuple)):
        res = '['
        empty = True
        for element in obj:
            if not empty:
                res += ', '
            res += dumps(element)
            empty = False
        res += ']'
        return res
    else:
        raise TypeError(f'Object of type {type(obj).__name__} is '
                        'not JSON serializable.')
