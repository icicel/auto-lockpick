from level.level import Level
from level_state import LevelState, Action

class Solver:
    level: Level
    solutions: "list[tuple[Action]]"

    def __init__(self, level: Level) -> None:
        self.level = level
        self.solutions = []
    
    def getSolutions(self) -> "list[tuple[Action]]":
        startState = LevelState.initialState(self.level)
        self.solve(startState)
        return self.solutions

    def getSolutionsAsStr(self) -> "list[str]":
        solutionsStr = []
        for solution in self.getSolutions():
            solutionsStr.append(", ".join([str(action) for action in solution]))
        return solutionsStr

    def solve(self, state: LevelState) -> None:
        for nextState in state.getNextStates():
            if nextState.isSolved():
                self.solutions.append(nextState.actions)
            else:
                self.solve(nextState)
        