
""" Reporter print the report message to terminal.
    The report format is like this:
        |{WhoReporting} |{WhatIsDoing}  |{StepIntro}

"""


class Reporter:

    def __init__(self, who: str, what: str):
        self.who = who
        self.what = what
        self.totalStep = None
        self.nowStep = 0
        self.totalSubstep = None
        self.nowSubstep = 0

    def initialize_stepIntro(self, totalStep: int):
        self.totalStep = totalStep
        self.nowStep = 0

    def initialize_substepIntro(self, totalSubstep: int):
        self.totalSubstep = totalSubstep
        self.nowSubstep = 0

    def report(self, withStepIntro=False, withSubstepIntro=False):
        printInfo = "|{}\t|{}".format(self.who, self.what)
        if withStepIntro == True:
            printInfo += " |{}/{}".format(self.nowStep, self.totalStep)
        if withSubstepIntro == True:
            printInfo += " |{}/{}".format(self.nowSubstep, self.totalSubstep)
        print(printInfo)
