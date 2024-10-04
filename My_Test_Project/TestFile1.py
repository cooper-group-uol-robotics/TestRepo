from .TestFile2 import testClass

class otherTestClass(testClass):
    def draw_a_cat():
        print("|\---/|")
        print("| o_o | ")
        print(" \_^_/ ")

    def draw_another_cat():
        cat = """
             |\_---_/|
            /   o_o   \
            |    U    |
            \  ._I_.  /
             `-_____-')
                
            """
        print(cat)