from src.InputListener import InputListener
from time import sleep


class AutomatedMouseKeyboardRoutine(object):
    def __init__(self, timeInSecondsBetweenEvents: float, numberOfTimesToRepeatRoutine: int):
        self.timeInSecondsBetweenEvents = timeInSecondsBetweenEvents
        self.numberOfTimesToRepeatRoutine = numberOfTimesToRepeatRoutine

    def Process(self):
        print("\n# End Subroutine: Left Control")
        print("# End Routine: Escape")

        print("\nListening...")
        inputListener = self.ListenInputs()
        print("\nRepeating...")
        for numberOfTimes in range(0, self.numberOfTimesToRepeatRoutine):
            self.RepeatInputs(inputListener)

    def ListenInputs(self) -> InputListener:
        inputListener = InputListener()
        isRoutineComplete = False
        while not isRoutineComplete:
            print("Press mouse key please...")
            inputListener.ListenOneMouseClick()
            print("Press keyboard key(s) (optional) and end subroutine...\n")
            isRoutineComplete = inputListener.ListenOneKeyPressed()
        return inputListener

    def RepeatInputs(self, inputListener: InputListener):
        for event in inputListener.events:
            event.process()
            sleep(self.timeInSecondsBetweenEvents)
