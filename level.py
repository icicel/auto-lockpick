from node import Node, NodeType

# Adds some amount of nodes as each other's neighbors
def makeNeighbors(*neighbors: Node) -> None:
    for a in neighbors:
        for b in neighbors:
            if a != b:
                a.addNeighbor(b)
                b.addNeighbor(a)

class Level:
    gameObjects: "dict[str, Node]"

    def __init__(self) -> None:
        self.gameObjects = {}
    
    # Add a created node to the level
    def addNode(self, node: Node, id: str) -> None:
        if id in self.gameObjects:
            raise Exception(f"Node with id {id} already exists")
        self.gameObjects[id] = node
        node.id = id

    # Create a node with a string id
    # Code format given in node.py
    def newNode(self, name: str, code: str) -> None:
        self.addNode(Node(code), name)

    # Create a chain of nodes between two nodes, or from one node (one-ended) if no end node is given
    # Also creates start and end nodes if they don't already exist
    def newChain(self, startName: str, endName: str, *codes: str) -> None:
        if not startName:
            raise Exception("Must have a start node")
        if not codes:
            # A chain of 0 nodes
            makeNeighbors(self.gameObjects[startName], self.gameObjects[endName])
            return

        nodes = [Node(code) for code in codes]

        if startName not in self.gameObjects:
            self.newNode(startName, None)
        makeNeighbors(self.gameObjects[startName], nodes[0])
        if endName:
            if endName not in self.gameObjects:
                self.newNode(endName, None)
            makeNeighbors(self.gameObjects[endName], nodes[-1])
            id = f"{startName}-{endName}"
        else:
            id = f"{startName}"

        for i in range(len(nodes)-1):
            makeNeighbors(nodes[i], nodes[i+1])
        
        # Add a bunch of apostrophes if ids conflict
        version = 0
        while id + "'" * version + "0" in self.gameObjects:
            version += 1
        for i, node in enumerate(nodes):
            self.addNode(node, id + "'" * version + str(i))
    
    # Tries to remove "space" nodes by connecting their neighbors with each other
    def clearSpace(self) -> None:
        x = []
        for id, node in self.gameObjects.items():
            if node.nodeType == NodeType.SPACE and id not in ["start", "end"]:
                for neighbor in node.neighbors:
                    neighbor.neighbors.remove(node)
                makeNeighbors(*node.neighbors)
                x.append(id)
        for id in x:
            del self.gameObjects[id]