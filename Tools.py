def MonteCarloTester(count, test):
    successCount = 0.0
    failCount = 0.0

    for i in range(count):
        test.takeSkillTest()
        if(test.result.outcome == "succeeded"):
            successCount += 1
        else:
            failCount += 1

    return successCount