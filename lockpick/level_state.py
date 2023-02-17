from level.level import Level
from level.node import Node
from level.node_enums import Color, NodeType, Effect
from action import Action, ActionType

# keys - amount of keys per color
# pool - list of nodes "available" in this state
# actions - list of actions taken to get to this state
# cursedNodes - list of nodes that are cursed
# openedNodes - list of IDs of nodes that have been opened
# cleanedNodes - list of IDs of nodes that have been cleaned
class LevelState:
    level: Level
    keys: "dict[Color, int]"
    pool: "list[Node]"
    actions: "list[Action]"
    cursedNodes: "list[Node]"
    openedNodes: "list[Node]"
    cleanedNodes: "list[Node]"

    def __init__(self, level: Level, keys: "dict[Color, int]", pool: "list[Node]", actions: "list[Action]", 
                cursedNodes: "list[Node]", openedNodes: "list[Node]", cleanedNodes: "list[Node]") -> None:
        self.level = level
        self.keys = keys
        self.pool = pool
        self.actions = actions
        self.cursedNodes = cursedNodes
        self.openedNodes = openedNodes
        self.cleanedNodes = cleanedNodes

    # Returns the starting state for a given level
    @classmethod
    def initialState(cls, level: Level) -> "LevelState":
        return LevelState(
            level,
            {color: 0 for color in range(Color.NUM_COLORS)},
            level.gameObjects[level.startNode.id].neighbors.copy(),
            [],
            [],
            [level.startNode],
            []
        )
    
    # Returns a new state with the given action applied
    # Tries to avoid copying lists if possible
    @classmethod
    def incState(cls, oldState: "LevelState", action: Action) -> "LevelState":
        if action.type == ActionType.OPEN or action.type == ActionType.MASTEROPEN:
            newKeys = oldState.keys.copy()
            newPool = oldState.pool.copy()
            newPool.remove(action.node)
            for neighbor in action.node.neighbors:
                if neighbor not in newPool and neighbor not in oldState.openedNodes:
                    newPool.append(neighbor)
            newOpenedNodes = oldState.openedNodes + [action.node]
        else:
            newKeys = oldState.keys
            newPool = oldState.pool
            newOpenedNodes = oldState.openedNodes

        if action.type == ActionType.CURSE or action.type == ActionType.BLESS:
            newCursedNodes = oldState.cursedNodes.copy()
        else:
            newCursedNodes = oldState.cursedNodes

        if action.type == ActionType.CLEAN:
            newCleanedNodes = oldState.cleanedNodes + [action.node]
        else:
            newCleanedNodes = oldState.cleanedNodes

        return LevelState(
            oldState.level,
            newKeys,
            newPool,
            oldState.actions + [action],
            newCursedNodes,
            newOpenedNodes,
            newCleanedNodes
        )
    
    def isSolved(self) -> bool:
        return self.level.endNode in self.pool
    
    def canClean(self, effect: Effect) -> bool:
        return {
            Effect.FROZEN: self.keys[Color.RED] > 0,
            Effect.PAINTED: self.keys[Color.BLUE] >= 3,
            Effect.ERODED: self.keys[Color.GREEN] >= 5
        }[effect]
    
    def getNextStates(self) -> "list[LevelState]":

        # Can nodes be cursed?
        if self.keys[Color.BROWN] > 0:
            for node in self.pool:
                if not node.isDoor() or node in self.cursedNodes or node.color in [Color.BROWN, Color.PURE]:
                    continue
                newState = LevelState.incState(self, Action(node, ActionType.CURSE))
                newState.cursedNodes.append(node)
                yield newState
        
        # Can nodes be blessed?
        if self.keys[Color.BROWN] < 0:
            for node in self.cursedNodes:
                newState = LevelState.incState(self, Action(node, ActionType.BLESS))
                newState.cursedNodes.remove(node)
                yield newState

        # Can nodes be cleaned?
        for node in self.pool:
            if node.effect != Effect.NONE and self.canClean(node.effect) and node not in self.cleanedNodes:
                newState = LevelState.incState(self, Action(node, ActionType.CLEAN))
                yield newState
        
        # Can nodes be master-opened?
        if self.keys[Color.GOLD] > 0:
            for node in self.pool:
                if not node.isDoor() or node.color in [Color.PURE, Color.GOLD]:
                    continue
                newState = LevelState.incState(self, Action(node, ActionType.MASTEROPEN))
                newState.keys[Color.GOLD] -= 1
                yield newState
        
        # Can nodes be opened?
        # Warning: very hard-coded
        for node in self.pool:
            # Can't open nodes with an effect unless they're cleaned
            if node.effect != Effect.NONE and node not in self.cleanedNodes:
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
                newState.keys[nodeColor] *= -1

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

            yield newState
