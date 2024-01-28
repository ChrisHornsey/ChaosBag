class SkillTest:
    def __init__(self, dificulty, skill, ChaosBag):
        self.dificulty = dificulty
        self.skill = skill
        self.ChaosBag = ChaosBag

        self.takeSkillTest()

    def takeSkillTest(self):
        draw = self.ChaosBag.drawToken()

        self.result = draw.Resolve(draw, self.skill, self.dificulty)
        
class SkillTestResult:
    def __init__(self, dificulty, result, outcome):
        self.dificulty = dificulty
        self.result = result
        self.outcome = outcome