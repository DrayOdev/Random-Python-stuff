# LOGIC GATES
gates = ["AND", "OR", "XOR", "NAND", "NOR" ]
global input_1
global input_2

class AND:
    def __init__(self, _0, _1):
        self._0 = 0
        self._1 = 0
        self.result = 0

    def parse(self, _0, _1):
        print(_0, _1)
        if _0 == 1 and _1 == 1:
            self.result = 1
        if self.result == 0:
            print("Gate parses 0")
        else:
            print("Gate parses 1")
class OR:
    def __init__(self, _0, _1):
        self._0 = 0
        self._1 = 0
        self.result = 0
    def parse(self, _0, _1):
        print(_0, _1)
        if (_0 == 1 and _1 == 0) or (_0 == 0 and _1 == 1) or (_0 == 1 and _1 == 1):
            self.result = 1
        if self.result == 0:
            print("Gate parses 0")
        else:
            print("Gate parses 1")
class XOR:
    def __init__(self, _0, _1):
        self._0 = 0
        self._1 = 0
        self.result = 0
    def parse(self, _0, _1):
        print(_0, _1)
        if (_0 == 1 and _1 == 0) or (_0 == 0 and _1 == 1):
            self.result = 1
            if self.result == 0:
                print("Gate parses 0")
            else:
                print("Gate parses 1")

def logic_gate():
    ANDCASE = AND(0,0)
    ORCASE = OR(0,0)
    print("please provide two inputs")
    input_1 = int(input("First input: "))
    input_2 = int(input("Second input: "))
    gate = input("Please provide a gate type: ").upper()
    match gate:
        case "AND":
                ANDCASE.parse(input_1, input_2)
        case "OR":
                ORCASE.parse(input_1, input_2)







logic_gate()
