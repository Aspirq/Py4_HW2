class HelloWord (object):
    def __init__(self):
        self.__hw_string = "Привет мир!"

    @property
    def hw_string(self):
        return self.__hw_string

    def __str__(self):
        return self.__hw_string

    __repr__ = __str__