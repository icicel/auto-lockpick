import level

# Puzzle 1-2
l = level.Level()
l.newChain("start", None,
    "K+.W"
)
l.newChain("start", None,
    "D+.W", "K+.O"
)
l.newChain("start", "end",
    "D+.W", "K+.W", "D+.O"
)

for id, node in l.gameObjects.items():
    print(id, str(node), [n.id for n in node.neighbors])