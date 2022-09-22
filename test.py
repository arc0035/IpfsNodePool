
class SingletonMeta(type):
    _instances = {}

    # __call__控制类的对象创建逻辑
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Demo(metaclass=SingletonMeta):
    pass

d1 = Demo()
d2 = Demo() # d1 ,d2 are same, becasue d2 is cached singleton