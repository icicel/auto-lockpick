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
    def incState(self, action: Action, isCursed: bool=False) -> "LevelState":

        if action.type == ActionType.OPEN:
            keys = self.keys.copy()
            pool = self.pool.copy()
            actions = self.actions + [action]
            openedNodes = self.openedNodes + [action.node]
            cursedNodes = self.cursedNodes
            cleanedNodes = self.cleanedNodes

            nodeAmount = action.node.amount
            nodeType = action.node.nodeType
            nodeColor = Color.BROWN if isCursed else action.node.color

            if nodeType == NodeType.KEY:
                keys[nodeColor] += nodeAmount
            elif nodeType == NodeType.KEYABS:
                keys[nodeColor] = nodeAmount       
            elif nodeType == NodeType.KEYFLIP:
                keys[nodeColor] *= -1
            elif nodeType == NodeType.DOOR:
                keys[nodeColor] -= nodeAmount
            elif nodeType == NodeType.DOORNEG:
                keys[nodeColor] -= nodeAmount
            elif nodeType == NodeType.DOORX:
                keys[nodeColor] = 0
            elif nodeType == NodeType.DOORNEGX:
                keys[nodeColor] = 0

            pool.remove(action.node)
            for neighbor in action.node.neighbors:
                if neighbor not in pool and neighbor not in self.openedNodes:
                    pool.append(neighbor)
        
        elif action.type == ActionType.MASTEROPEN:
            keys = self.keys.copy()
            pool = self.pool.copy()
            actions = self.actions + [action]
            openedNodes = self.openedNodes + [action.node]
            cursedNodes = self.cursedNodes
            cleanedNodes = self.cleanedNodes
            
            keys[Color.GOLD] -= 1
            pool.remove(action.node)
            for neighbor in action.node.neighbors:
                if neighbor not in pool and neighbor not in self.openedNodes:
                    pool.append(neighbor)
        
        elif action.type == ActionType.CLEAN:
            keys = self.keys
            pool = self.pool
            actions = self.actions + [action]
            openedNodes = self.openedNodes
            cursedNodes = self.cursedNodes
            cleanedNodes = self.cleanedNodes + [action.node]

        elif action.type == ActionType.CURSE:
            keys = self.keys
            pool = self.pool
            actions = self.actions + [action]
            openedNodes = self.openedNodes
            cursedNodes = self.cursedNodes + [action.node]
            cleanedNodes = self.cleanedNodes
        
        elif action.type == ActionType.BLESS:
            keys = self.keys
            pool = self.pool
            actions = self.actions + [action]
            openedNodes = self.openedNodes
            cursedNodes = self.cursedNodes.copy()
            cleanedNodes = self.cleanedNodes

            cursedNodes.remove(action.node)

        return LevelState(
            self.level,
            keys,
            pool,
            actions,
            cursedNodes,
            openedNodes,
            cleanedNodes
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
                yield self.incState(Action(node, ActionType.CURSE))
        
        # Can nodes be blessed?
        if self.keys[Color.BROWN] < 0:
            for node in self.cursedNodes:
                yield self.incState(Action(node, ActionType.BLESS))

        # Can nodes be cleaned?
        for node in self.pool:
            if node.effect == Effect.NONE or not self.canClean(node.effect) or node in self.cleanedNodes:
                continue
            yield self.incState(Action(node, ActionType.CLEAN))
        
        # Can nodes be master-opened?
        if self.keys[Color.GOLD] > 0:
            for node in self.pool:
                if not node.isDoor() or node.color in [Color.PURE, Color.GOLD]:
                    continue
                yield self.incState(Action(node, ActionType.MASTEROPEN))
        
        # Can nodes be opened?
        # Warning: very hard-coded
        for node in self.pool:
            # Can't open nodes with an effect unless they're cleaned
            if node.effect != Effect.NONE and node not in self.cleanedNodes:
                continue
            # Cursed nodes act like brown nodes
            isCursed = node in self.cursedNodes
            nodeColor = Color.BROWN if isCursed else node.color
            
            if node.nodeType == NodeType.DOOR and self.keys[nodeColor] < node.amount:
                continue
            if node.nodeType == NodeType.DOORNEG and self.keys[nodeColor] > node.amount:
                continue
            if node.nodeType == NodeType.DOORBLANK and self.keys[nodeColor] != 0:
                continue
            if node.nodeType == NodeType.DOORX and self.keys[nodeColor] < 1:
                continue
            if node.nodeType == NodeType.DOORNEGX and self.keys[nodeColor] > -1:
                continue

            yield self.incState(Action(node, ActionType.OPEN), isCursed=isCursed)
