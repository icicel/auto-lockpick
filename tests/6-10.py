import lockpick.solver as solver

l = solver.Level("S", "E")

l.newChain("S", "E", "D25.X")
l.newNeighbor("S", "K.M")
l.newNeighbor("r", "K-6.X")
l.newChain("S", "r",
    "DX.l", "K.B", "D.X", "K4.X", "D3.BP"
)
l.newChain("S", "r",
    "DX.X", "K4.X", "D2.X", "K.B", "D-X.c"
)
l.newChain("S", "r",
    "K-5.l", "D-X.l", "K5.X", "DO.B", "K!.c", "D3.c", "K3.Y", "D.X"
)
l.newChain("S", "r",
    "K9.c", "D3.c", "K.B", "DO.lP", "K!.X", "DO.lP", "K-4.X", "K!.X", "D-3.M", "K4.X", "DO.Y"
)
l.newChain("S", "r",
    "D-4.l", "K4.l", "D-X.c", "K!.X", "D3.X", "K3.X", "K=0.B", "K!.c", "D-3.X"
)

print(solver.Solver(l).getSolutionsAsStr())
