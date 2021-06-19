class Cell:
    def __init__(self, value = -1):
        self.domain = [1,0]
        self.value = value
        if value != -1 :
            self.satisfied = True
        else :
            self.satisfied = False
        self.maclist = []