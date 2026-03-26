# LOGIC GATES
gates = ["AND", "OR", "XOR", "NAND", "NOR" ]
conditions = ["A:", "B:", "Gates:"]
global A
global B
file = open("save.txt", "a+")

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
    if file.readlines() != "":
        q = input("ERR- FILE DETECTED! Would you like to wipe the file?: [y/n] ")
        if q == "y":
            file.truncate(0)
        else:
            return

def logic_gate():
    ANDCASE = AND(0,0)
    ORCASE = OR(0,0)
    XORCASE = XOR(0,0)
    NANDCASE = NAND(0,0)
    NORCASE = NOR(0, 0)
    print("please provide two inputs")
    A = int(input("First input: "))
    B = int(input("Second input: "))
    gate = input("Please provide a gate type: ").upper()
    match gate:
        case "AND":
                ANDCASE.parse(A, B)
        case "OR":
                ORCASE.parse(A, B)
        case "XOR":
                XORCASE.parse(A, B)
        case "NAND":
            NANDCASE.parse(A, B)
        case "NOR":
            NORCASE.parse(A, B)
        case "1":
            ANDCASE.parse(A, B)
        case "2":
            ORCASE.parse(A, B)
        case "3":
            XORCASE.parse(A, B)
        case "4":
            NANDCASE.parse(A, B)
        case "5":
            NORCASE.parse(A, B)
    file.write("A:\n")
    file.write(str(A)+"\n")
    file.write("B:\n")
    file.write(str(B)+"\n")
    file.write("Gate:\n"+str(gate)+"\n")
    print("If you encounter any mistakes with this interpreter please create an issue on my Github :D ")
    again = input("Do you want to continue? (y/n): ")
    if again == "y":
        logic_gate()
        file.seek(0)
        print(file.readline())
    elif again != "y":
        file.seek(0)
        for line in file:
            print(line.rstrip("\n"))
        print("Thank you for using the program")





start()
logic_gate()


