class ChaosToken:
    def __init__(self, modifier, name=""):
        self.mod = modifier
        if(name == ""):
            self.name = str(modifier)
        else:
            self.name = name