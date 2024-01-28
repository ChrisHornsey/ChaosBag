import SkillTest

class ChaosToken:
    def __init__(self, modifier, name="", type="Regular"):
        self.mod = modifier
        if(name == ""):
            self.name = str(modifier)
        else:
            self.name = name

        if type == "Regular":
            self.Resolve = StandardResolution



def StandardResolution(token, skillValue, dificulty):
    result = skillValue + token.mod

    if(result < dificulty):
        outcome = "failed"
    else:
        outcome = "succeeded"

    return SkillTest.SkillTestResult(dificulty, result, outcome)