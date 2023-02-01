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

solutions = solver.Solver(l).getSolutionsAsStr()
for solution in solutions:
    print(solution)