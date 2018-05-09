def flatten_dictionary(dictionary):
    def inner(key, value):
        if isinstance(value, dict):
            if key:
                result = []
                for k, v in flatten_dictionary(value).items():
                    if k:
                        result.append((key + '.' + k, v))
                    else:
                        result.append((key, v))
                return result
            else:
                return [(k, v) for k, v in flatten_dictionary(value).items()]
        else:
            return [(key, value)]

    items = [i for k, v in dictionary.items() for i in inner(k, v)]
    return dict(items)


def flatten_dictionary(dictionary):
    result = dict()

    def loop(d, mainkey=''):
        for k, v in d.items():
            if k:
                if mainkey:
                    k = mainkey + '.' + k
            else:
                k = mainkey

            if isinstance(v, dict):
                loop(v, k)
            else:
                result[k] = v

    loop(dictionary)
    return result