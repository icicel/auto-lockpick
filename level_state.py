from node import *

# keys - amount of keys per color
# pool - list of nodes "available" in this state
# curseState - 0 = no curse, 1 = curse, -1 = negated curse
class LevelState:
    keys: "dict[Color, int]"
    pool: "list[Node]"
    curseState: int
    actions: "tuple[Node]"

    def __init__(self, pool: "list[Node]") -> None:
        self.keys = {color: 0 for color in range(Color.NUM_COLORS)}
        self.pool = pool
        self.curseState = 0
        self.actions = ()
    
    def getNextStates(self) -> "list[LevelState]":
        # TODO
        return []
    
    def isSolved(self) -> bool:
        # TODO
        return False