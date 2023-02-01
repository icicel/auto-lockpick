from level import Level, Node
from level_state import LevelState

class Solver:
    level: Level
    solutions: "list[tuple[Node]]"

    def __init__(self, level: Level) -> None:
        self.level = level
        self.solutions = []
    
    def getSolutions(self) -> "list[tuple[Node]]":
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
        