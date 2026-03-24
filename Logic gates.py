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
        if self.result == 1:
            print("Gate parses 1")
        else:
            print("Gate parses 0")
class NAND:
    def __init__(self, _0, _1):
        self._0 = 0
        self._1 = 0
        self.result = 0
    def parse(self, _0, _1):
        print(_0, _1)
        if (_0 == 1 and _1 == 0):
            self.result = 1
        if self.result == 1:
            print("Gate parses 1")
        else:
            print("Gate parses 0")
class NOR:
    def __init__(self, _0, _1):
        self._0 = 0
        self._1 = 0
        self.result = 0
    def parse(self, _0, _1):
        print(_0, _1)
        if (_0 == 0 and _1 == 0):
            self.result = 1
        if self.result == 1:
            print("Gate parses 1")
        else:
            print("Gate parses 0")

def start():
    print("This is a logic gate interpreter. \nThis will show you how each gate functions")
    print("Below are the supported gate types.")
    print("____________________________________________________________________________")
    print("1. AND\n2. OR\n3. XOR\n4. NAND\n5. NOR")


def logic_gate():
    ANDCASE = AND(0,0)
    ORCASE = OR(0,0)
    XORCASE = XOR(0,0)
    NANDCASE = NAND(0,0)
    NORCASE = NOR(0, 0)
    print("please provide two inputs")
    input_1 = int(input("First input: "))
    input_2 = int(input("Second input: "))
    gate = input("Please provide a gate type: ").upper()
    match gate:
        case "AND":
                ANDCASE.parse(input_1, input_2)
        case "OR":
                ORCASE.parse(input_1, input_2)
        case "XOR":
                XORCASE.parse(input_1, input_2)
        case "NAND":
            NANDCASE.parse(input_1, input_2)
        case "NOR":
            NORCASE.parse(input_1, input_2)
        case "1":
            ANDCASE.parse(input_1, input_2)
        case "2":
            ORCASE.parse(input_1, input_2)
        case "3":
            XORCASE.parse(input_1, input_2)
        case "4":
            NANDCASE.parse(input_1, input_2)
        case "5":
            NORCASE.parse(input_1, input_2)
    print("If you encounter any mistakes with this interpreter please create an issue on my Github :D ")
    again = input("Do you want to continue? (y/n): ")
    if again == "y":
        logic_gate()
    else:
        print("Thank yo")





start()
logic_gate()
