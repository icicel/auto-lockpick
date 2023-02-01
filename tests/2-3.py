import lockpick.solver as solver

l = solver.Level("S", "E")
l.newNeighbor("S", "K.M")
l.newChain("S", "m"
    "D.o", "K.G", "D.G", "K.M", "D.w"
)
l.newChain("S", "m"
    "D.w", "K.o", "D.l", "K.M", "D.R", "K.G", "D.l"
)
l.newChain("S", "m"
    "D.l", "K.G", "D.G", "K.o", "D.o", "K.l", "D.w", "K.l", "D.l"
)
l.newChain("S", "m"
    "D.G", "K.w", "D.o", "K.o", "D.l", "K.w", "D.w", "K.M", "D.G", "K.o", "D.o"
)
l.newNeighbor("m", "K.M")
l.newChain("m", "E"
    "D.R", "K.w", "D.c", "K.G", "D.p", "K.l", "D.B"
)

solutions = solver.Solver(l).getSolutionsAsStr()
for solution in solutions:
    print(solution)
    