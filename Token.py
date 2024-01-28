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
        elif type == "Autofail":
            self.Resolve = AutofailResolution



def StandardResolution(token, skillValue, dificulty):
    result = skillValue + token.mod

    if(result < dificulty):
        outcome = "failed"
    else:
        outcome = "succeeded"

    return SkillTest.SkillTestResult(dificulty, result, outcome)

def AutofailResolution(token, skillValue, dificulty):
    return SkillTest.SkillTestResult(dificulty, 0, "failed")