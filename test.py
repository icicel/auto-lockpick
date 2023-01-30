import level

l = level.Level()

l.newChain("start", "A",
    "K+.W"
)
l.newChain("start", "A",
    "D+.W", "K+.O"
)
l.newChain("start", "end",
    "D+.W", "K+.W", "D+.O"
)
l.newChain("A", None,
    "K+69.b", "D+69.b"
)
l.clearSpace()

for id, node in l.gameObjects.items():
    print(id, str(node), [n.id for n in node.neighbors])