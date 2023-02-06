import lockpick.solver as solver

l = solver.Level("S", "Z")

# A
l.newChain("S", "A1",
    "K2.M", "K.w", "K8.l"
)
l.newChain("A1", "A2",
    "D2.c", "D.w", "D.l", "K!.G", "D.w", "DX.o"
)
l.newChain("A1", "A2",
    "D.p", "D.w", "D-X.o", "D12.p", "K-12.c"
)
l.newChain("A2", None,
    "K!.B", "K.X"
)
# B
l.newChain("A1", "B1",
    "DO.w", "D-2.c", "DO.M", "K=.o"
)
l.newChain("B1", "B2",
    "K.w"
)
l.newChain("B2", None,
    "D.w", "K=-1.o", "K=-1.o", "D.cF", "D.cF", "K-5.G", "K.X"
)
l.newChain("B2", None,
    "D-3.Y", "D-X.o", "D.p", "D.w", "D8.c", "K.X"
)
# C
l.newChain("B1", "C1",
    "K.M", "D.w", "DO.o", "DO.o", "DO.M"
)
l.newChain("C1", None,
    "D4.p", "D2.c", "DX.o", "D.B", "D-6.l", "D.w", "DO.oF", "K.X"
)
l.newChain("C1", "C2",
    "K4.c", "K2.w"
)
l.newChain("C2", "C3",
    "D2.cP", "D.w", "D-1.l", "K.w", "D4.G", "DO.B"
)
l.newChain("C2", "C3",
    "D2.c", "D.w", "D.l", "K17.p", "D12.p", "D3.c"
)
l.newChain("C3", None,
    "K.R", "K.X"
)
# D
l.newChain("C2", "D1",
    "K2.M", "K=.o", "DO.w", "DO.c", "DO.c", "DO.o", "DO.o", "DO.o", "DO.M", "K6.c", "K.B"
)
l.newNeighbor("D1", "K!.l")
l.newChain("D1", None,
    "D6.l", "K2.w", "DO.oP", "K.X"
)
l.newChain("D1", "D2",
    "K3.M", "D12.p", "D.B", "D-1.l", "K2.w", "K=-1.o"
)
l.newChain("D2", None,
    "DO.l", "D.B", "DO.oE", "K.X"
)
# E
l.newChain("D2", "E1",
    "K31.p", "DO.o", "DO.o", "DO.M", "K.M"
)
l.newChain("E1", None,
    "D.R", "D-3.Y", "DO.B", "K-5.G"
)
l.newChain("E1", "E2",
    "D4.p", "K2.w", "D-1.l", "D.cE", "D.cE"
)
l.newChain("E1", "E2",
    "D.B", "D12.G", "D.l", "K-99.Y", "D.c"
)
l.newChain("E2", None,
    "DO.o", "K2.B", "K.X"
)
# F
l.newChain("E1", "F1",
    "D.w", "D.w", "D4.c", "K=.o", "DO.M", "K2.M"
)
l.newChain("F1", "F2",
    "DO.c", "D.w", "DX.o", "D.p", "DO.w"
)
l.newChain("F1", "F2",
    "D.l", "D.l", "D-12.c", "DO.o", "DO.w", "D-1.l", "D-1.l"
)
l.newChain("F2", None,
    "K!.R", "D.R", "DX.G", "D.w", "K!.c", "K.X"
)
# P
l.newChain("F2", "P",
    "DO.R", "DO.w", "DO.M"
)
l.newChain("P", None,
    "K=.o", "DO.wF", "D-X.G", "DO.c", "DO.c", "K.X"
)
l.newChain("P", "Z",
    "K5.M", "D10.X", "DO.M", "DO.o", "DO.p", "DO.R", "DO.G", "DO.B", "K92.Y", "DO.Y"
)

print(solver.Solver(l).getSolutionsAsStr())