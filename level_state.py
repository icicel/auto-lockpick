from node import *

# keys - amount of keys per color
# pool - list of nodes "available" in this state
class LevelState:
    keys: "dict[Color, int]"
    pool: "list[Node]"
    actions: "tuple[Node]"

    def __init__(self, pool: "list[Node]") -> None:
        self.keys = {color: 0 for color in range(Color.NUM_COLORS)}
        self.pool = pool
        self.actions = ()
    
    def getNextStates(self) -> "list[LevelState]":
        # TODO
        return []
