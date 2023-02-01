import solver

# Puzzle 1-2
l = solver.Level("start", "end")
l.newChain("start", None,
    "K.w"
)
l.newChain("start", None,
    "D.w", "K.o"
)
l.newChain("start", "end",
    "D.w", "K.w", "D.o"
)

for id, node in l.gameObjects.items():
    print(id, str(node), [n.id for n in node.neighbors])
solutions = solver.Solver(l).getSolutions()
for solution in solutions:
    print([node.asCode() for node in solution])