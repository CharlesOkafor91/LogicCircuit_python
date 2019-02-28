

class LogicGate:

    def __init__(self, name):
        self.label = name
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter the value of pin A for " + self.getLabel() + " gate --> "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter the value of pin B for " + self.getLabel() + " gate --> "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("CANNOT CONNECT: No empty pins on this Gate!!!")


class AndGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter the value of pin for " + self.getLabel() + " gate --> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("CANNOT CONNECT: No empty pin on this Gate!!!")

class NotGate(UnaryGate):

    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.toGate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    g5 = OrGate("G5")
    g6 = AndGate("G6")
    c1 = Connector(g1,g2)
    c2 = Connector(g4,g3)
    c3 = Connector(g1,g2)
    c4 = Connector(g1,g3)
    c5 = Connector(g2,g5)
    c6 = Connector(g3,g5)
    c7 = Connector(g5,g6)
    print("The final output is "+str(g6.getOutput()))

main()

# g1 = AndGate("G!")
# g1.getOutput()

