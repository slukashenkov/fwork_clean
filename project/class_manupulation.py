"""
Quickly learn python class and
class method`s syntax
as well
as good habits of commenting and documenting
as you go
"""

class DoProbeClass:
    """
    Do probe class tryies all the basic things
    that classes suppose to do
    And first thing is how you can define
    some fields of the class before using them
    """
    str_tuple=("""one elem""", """two elem""", """three elem""")
    counter=0

    def __init__(self,
                 field01=None,
                 field02=None,
                 field03=None):

        self.field01=field01
        self.field02=field02
        self.field03=field03

        type(self).counter+=1
        print("Here is a counter setup "+str(self.counter)+"\n")

    def __del__(self):
        type(self).counter -= 1
        print("Here is a potential cleanup "+str(self.counter)+"\n")

    '''This type of method requires instantination'''
    def try_print_fields(self):
        print("fields set for the class: \n"
        +"\n"+str(self.field01)
        +"\n"+str(self.field02)
        +"\n"+str(self.field03)
        +"\n")

    ''' Method that would not on the instance'''
    def class_only_method():
        print("only can use those with class directly \n")

    '''Static method available as ???'''
    @staticmethod
    def static_method_example():
        print("example that shows static method`s power \n")


class PropDemoClass:

    def __init__(self, a, b):
        self.attr01=a
        self.attr02=b

    @property
    def attr02(self):
        return self.__attr02

    @attr02.setter
    def attr02(self,val):
        if val < 0:
            self.__attr02 = 0
        elif val > 9:
            self.__attr02=9
        else:
            self.__attr02 = val


if __name__=="__main__":
    dpr=DoProbeClass("Set field 1 as String", 222, 7889)
    dpr.try_print_fields()

    '''can access assigned elem dir from the class or instance'''
    for number, text in enumerate(dpr.str_tuple):
        print(str(number)+ " " + text + "\n")

    dpr01=DoProbeClass()
    dpr02=DoProbeClass()
    dpr03=DoProbeClass()

    DoProbeClass.class_only_method()
    DoProbeClass.static_method_example()
    dpr.static_method_example()

    pdc=PropDemoClass(23, 15)
    print("plain attribute "+str(pdc.attr01)+"\n")
    print("pdc set val: " + str(pdc.attr02) + "\n")

    pdc = PropDemoClass(1, 12)
    print("plain attribute " + str(pdc.attr01) + "\n")
    print("pdc set val: "+str(pdc.attr02) + "\n")
