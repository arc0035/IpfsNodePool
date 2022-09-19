def singleton(cls):
    instances = dict()

    def init(*args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)
        return instances[cls]

    return init
