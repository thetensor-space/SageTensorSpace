import SageTensorSpace as TS
MS = MatrixSpace(GF(7), 5, 6)
M = MS.random_element()
t = TS.TensorFromMatrices([M], 2, 1)

# Testing a property
U = VectorSpace(GF(7), 5)
V = VectorSpace(GF(7), 6)
assert all(M[i][j] == t((U.basis()[i], V.basis()[j]))[0] for i in range(5) for j in range(6))
