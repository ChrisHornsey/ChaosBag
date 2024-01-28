class SkillTest:
    def __init__(self, dificulty, skill, ChaosBag):
        self.dificulty = dificulty
        self.skill = skill
        self.ChaosBag = ChaosBag

        self.takeSkillTest()

    def takeSkillTest(self):
        draw = self.ChaosBag.drawToken()

        result = self.skill + draw.mod

        if(result < self.dificulty):
            outcome = "failed"
        else:
            outcome = "succeeded"

        self.result = SkillTestResult(self.dificulty, result, outcome)
        
class SkillTestResult:
    def __init__(self, dificulty, result, outcome):
        self.dificulty = dificulty
        self.result = result
        self.outcome = outcome