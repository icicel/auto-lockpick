from level import Level
from level_state import LevelState, Action

class Solver:
    level: Level
    solutions: "list[tuple[Action]]"

    def __init__(self, level: Level) -> None:
        self.level = level
        self.solutions = []
    
    def getSolutions(self) -> "list[tuple[Action]]":
        startPool = self.level.gameObjects[self.level.startNode].neighbors
        startState = LevelState(startPool)
        self.solve(startState)
        return self.solutions
        
    def solve(self, state: LevelState) -> None:
        for nextState in state.getNextStates():
            for node in nextState.pool:
                if node.id == self.level.endNode:
                    self.solutions.append(nextState.actions)
                    return
            else:
                self.solve(nextState)
        