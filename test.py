
class Parent:
    def __init__(self):
        print('Parent')


class Son(Parent):
    def __init__(self):
        # Parent.__init__(self) # method 1
        # super(Son, self).__init__() # method 2
        print('son')

s = Son()

