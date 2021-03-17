
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

    def initialize_stepIntro(self, totalStep: int):
        self.totalStep = totalStep
        self.nowStep = 0

    def report(self, withStepIntro=False):
        if withStepIntro == False:
            print("|{}\t|{}".format(self.who, self.what))
        else:
            self.nowStep += 1
            print("|{}\t|{}\t|{}/{}".format(self.who,
                                            self.what, self.nowStep, self.totalStep))
