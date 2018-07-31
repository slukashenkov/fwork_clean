class BasicFunctions:

    def __init__(self):
        self.y=5

    def basic_funct_for_test(self):
        x=9
        if x != 0:
            return x * self.y
        else:
            return super.y * self.y

if __name__ == "__main__":
    bf=BasicFunctions()
    result=bf.basic_funct_for_test()
    print(result)