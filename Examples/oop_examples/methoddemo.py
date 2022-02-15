class MethodDemo:
    a = 1

    @classmethod
    def classN(cls):
        print("Class Method. cls.a = ", cls.a)

    @staticmethod
    def staticN():
        print("Static Method")


MethodDemo.classN()
md1 = MethodDemo()
md1.classN()

md1.staticN()
MethodDemo.staticN()


