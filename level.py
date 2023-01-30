from node import Node

class Level:
    gameObjects: dict

    def __init__(self):
        self.gameObjects = {}

    def newNode(self, name, code):
        self.gameObjects[name] = Node(code)

    def newConnection(self, start, end, *codes):
        if start not in self.gameObjects:
            self.gameObjects[start] = Node()
        if end not in self.gameObjects:
            self.gameObjects[end] = Node()