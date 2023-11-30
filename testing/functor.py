



class Myfunctor:
    def __init__(self, n = 10):
        self.n =  n 
    def __call__(self,x):
        if type(x) == str:
            self.__string(x)
        if type(x) == int:
            self.__integer(x)
    @staticmethod
    def __string(info):
        print("es aris stringi")
    @staticmethod
    def __integer(info):
        print("es aris integeri")

class CallFunctor:
    def __init__(self):
        self.my_obj = Myfunctor()
    def check_type(self,info):
        self.my_obj(info)
call = CallFunctor()
call.check_type('f')

class Myfunctor:
    def __init__(self, n=10):
        self.n = n

    def __call__(self, x):
        if isinstance(x, str):
            Myfunctor.__string(x)
        elif isinstance(x, int):
            Myfunctor.__integer(x)

    @staticmethod
    def __string(info):
        print("This is a string")

    @staticmethod
    def __integer(info):
        print("This is an integer")

class CallFunctor:
    def __init__(self):
        self.my_obj = Myfunctor()

    def check_type(self, info):
        self.my_obj(info)

call = CallFunctor()
call.check_type('f')