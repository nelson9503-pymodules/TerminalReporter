# TerminalReporter

TerminalReporter print the report message to terminal. The format of message is like this:
`|Who   |What   |Step`

## Quick Start

```python
import TerminalReporter

reporter = TermainalReporter.Reporter("StepManager", "Introducing steps...") # who & what

# initialize the steps introduction
reporter.initialize_stepIntro(100) # sum of steps

for _ in range(100):
    reporter.report(withStepIntro=True)
```

Outputs will like this:

```bash
|StepManager    |Introducing steps...   |1/100
|StepManager    |Introducing steps...   |2/100
|StepManager    |Introducing steps...   |3/100
|StepManager    |Introducing steps...   |4/100
```
