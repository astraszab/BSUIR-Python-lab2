def singleton(cls):
    """Change class behavior to singleton.
    Singleton can have only one instance.
    """
    def singleton_constructor(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = old_constructor(cls)
        return cls.instance
    old_constructor = cls.__new__
    cls.__new__ = singleton_constructor
    return cls


@singleton
class A:
    def __init__(self):
        pass
