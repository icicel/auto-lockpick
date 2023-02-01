import solver

l = solver.Level("S", "E")
l.newNeighbor("S", "K.M")
l.newChain("S", "m"
    "D.o", "K.g", "D.g", "K.M", "D.w"
)
l.newChain("S", "m"
    "D.w", "K.o", "D.l", "K.M", "D.R", "K.g", "D.l"
)
l.newChain("S", "m"
    "D.l", "K.g", "D.g", "K.o", "D.o", "K.l", "D.w", "K.l", "D.l"
)
l.newChain("S", "m"
    "D.g", "K.w", "D.o", "K.o", "D.l", "K.w", "D.w", "K.M", "D.g", "K.o", "D.o"
)
l.newNeighbor("m", "K.M")
l.newChain("m", "E"
    "D.R", "K.w", "D.c", "K.g", "D.p", "K.l", "D.B"
)

solutions = solver.Solver(l).getSolutionsAsStr()
for solution in solutions:
    print(solution)