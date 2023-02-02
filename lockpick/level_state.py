from level.level import Level
from level.node import Node
from level.node_enums import Color, NodeType, Effect
from action import Action, ActionType

# keys - amount of keys per color
# pool - list of nodes "available" in this state
# actions - list of actions taken to get to this state
# cursedNodes - list of nodes that are cursed
# openedNodes - list of IDs of nodes that have been opened
class LevelState:
    level: Level
    keys: "dict[Color, int]"
    pool: "list[Node]"
    actions: "tuple[Action]"
    cursedNodes: "list[Node]"
    openedNodes: "list[str]"

    def __init__(self, level: Level, keys: "dict[Color, int]", pool: "list[Node]", actions: "tuple[Action]", cursedNodes: "list[Node]", openedNodes: "list[str]") -> None:
        self.level = level
        self.keys = keys
        self.pool = pool
        self.actions = actions
        self.cursedNodes = cursedNodes
        self.openedNodes = openedNodes

    # Returns the starting state for a given level
    @classmethod
    def initialState(cls, level: Level) -> "LevelState":
        return LevelState(
            level,
            {color: 0 for color in range(Color.NUM_COLORS)},
            level.gameObjects[level.startNode].neighbors,
            (),
            [],
            []
        )
    
    # Returns a new state with the given action applied
    @classmethod
    def incState(cls, oldState: "LevelState", action: Action) -> "LevelState":
        if action.type == ActionType.OPEN or action.type == ActionType.MASTEROPEN:
            newPool = oldState.pool.copy()
            newPool.remove(action.node)
            for neighbor in action.node.neighbors:
                if neighbor not in newPool and neighbor.id not in oldState.openedNodes:
                    newPool.append(neighbor)
            return LevelState(
                oldState.level,
                oldState.keys.copy(),
                newPool,
                oldState.actions + (action,),
                oldState.cursedNodes.copy(),
                oldState.openedNodes + [action.node.id]
            )         
        return LevelState(
            oldState.level,
            oldState.keys.copy(),
            oldState.pool.copy(),
            oldState.actions + (action,),
            oldState.cursedNodes.copy(),
            oldState.openedNodes.copy()
        )
    
    def isSolved(self) -> bool:
        for node in self.pool:
            if node.id == self.level.endNode:
                return True
        return False
    
    def getNextStates(self) -> "list[LevelState]":
        nextStates: "list[LevelState]" = []

        # Can nodes be cursed?
        if self.keys[Color.BROWN] > 0:
            for node in self.pool:
                if node in self.cursedNodes or node.color in [Color.BROWN, Color.PURE]\
                or node.isKey() or node.nodeType == NodeType.SPACE:
                    continue
                newState = LevelState.incState(self, Action(node, ActionType.CURSE))
                newState.cursedNodes.append(node)
                nextStates.append(newState)
        
        # Can nodes be blessed?
        if self.keys[Color.BROWN] < 0:
            for node in self.cursedNodes:
                newState = LevelState.incState(self, Action(node, ActionType.BLESS))
                newState.cursedNodes.remove(node)
                nextStates.append(newState)

        # Can nodes be cleaned?
        if self.keys[Color.RED] > 0:
            for node in self.pool:
                if node.effect == Effect.FROZEN and Action(node, ActionType.CLEAN) not in self.actions:
                    newState = LevelState.incState(self, Action(node, ActionType.CLEAN))
                    nextStates.append(newState)
        if self.keys[Color.BLUE] >= 3:
            for node in self.pool:
                if node.effect == Effect.PAINTED and Action(node, ActionType.CLEAN) not in self.actions:
                    newState = LevelState.incState(self, Action(node, ActionType.CLEAN))
                    nextStates.append(newState)
        if self.keys[Color.GREEN] >= 5:
            for node in self.pool:
                if node.effect == Effect.ERODED and Action(node, ActionType.CLEAN) not in self.actions:
                    newState = LevelState.incState(self, Action(node, ActionType.CLEAN))
                    nextStates.append(newState)
        
        # Can nodes be master-opened?
        if self.keys[Color.GOLD] > 0:
            for node in self.pool:
                if node.isDoor() and node.color not in [Color.PURE, Color.GOLD]:
                    newState = LevelState.incState(self, Action(node, ActionType.MASTEROPEN))
                    newState.keys[Color.GOLD] -= 1
                    nextStates.append(newState)
        
        # Can nodes be opened?
        # Warning: very hard-coded
        for node in self.pool:
            # Can't open nodes with an effect unless they're cleaned
            if node.effect != Effect.NONE and Action(node, ActionType.CLEAN) not in self.actions:
                continue
            # Can't open spaces
            if node.nodeType == NodeType.SPACE:
                continue
            # Cursed nodes act like brown nodes
            if node in self.cursedNodes:
                nodeColor = Color.BROWN
            else:
                nodeColor = node.color

            newState = LevelState.incState(self, Action(node, ActionType.OPEN))

            if node.nodeType == NodeType.KEY:
                newState.keys[nodeColor] += node.amount

            elif node.nodeType == NodeType.KEYABS:
                newState.keys[nodeColor] = node.amount
                
            elif node.nodeType == NodeType.KEYFLIP:
                newState.keys[nodeColor] = -newState.keys[nodeColor]

            elif node.nodeType == NodeType.DOOR:
                if self.keys[nodeColor] < node.amount:
                    continue
                newState.keys[nodeColor] -= node.amount

            elif node.nodeType == NodeType.DOORNEG:
                if self.keys[nodeColor] > node.amount:
                    continue
                newState.keys[nodeColor] += node.amount

            elif node.nodeType == NodeType.DOORBLANK:
                if self.keys[nodeColor] != 0:
                    continue

            elif node.nodeType == NodeType.DOORX:
                if self.keys[nodeColor] <= 0:
                    continue
                newState.keys[nodeColor] = 0

            elif node.nodeType == NodeType.DOORNEGX:
                if self.keys[nodeColor] >= 0:
                    continue
                newState.keys[nodeColor] = 0

            nextStates.append(newState)
            

        return nextStates