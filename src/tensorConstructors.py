#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from globalVars import _is_int
from frameConstructors import FreeRFrame as _FreeRFrame
from sage.all import vector as _vector
from sage.all import Matrix as _Matrix
from sage.all import transpose as _transpose
from tensorStructureConstants import _next_gen
from tensorClass import Tensor as _Tensor


# Copied and translated from 
# github.com/thetensor-space/TensorSpace/Tensor/Tensor.m
def _sequence_as_tensor(R, dims, S):
    # Some initial set up
    v = len(dims)
    c = dims[-1]
    dims_dom = dims[:-1]
    mult = lambda x, y: x*y
    add = lambda x, y: x + y
    offsets = [reduce(mult, dims[i+1:], 1) for i in range(v - 1)] + [1]

    # The actual eval function
    def F(x):
        assert len(x) == v-1
        vec = [0 for i in range(c)]
        curr = [1 for i in range(v-1)]
        for i in range(c):
            while curr[0] != 0:
                ind = [j-1 for j in curr] + [i]
                entry = reduce(add, [z[0]*z[1] for z in zip(ind, offsets)])
                consts = [x[j][curr[j]-1] for j in range(len(x))]
                vec[i] += reduce(mult, consts, S[entry])
                curr = _next_gen(dims_dom, curr)
        return _vector(R, vec)
    return F

# Copied and translated from 
# github.com/thetensor-space/TensorSpace/Tensor/Tensor.m
def _matrices_to_sequence(Mats, a, b):
    x = Mats[0].nrows()
    y = Mats[0].ncols()
    z = len(Mats)

    if {a, b} == {1, 2}:
        S = [Mats[k][i][j] for i in range(x) for j in range(y) \
            for k in range(z)]
        dims = [x, y, z]
    elif {a, b} == {0, 2}:
        S = [Mats[k][i][j] for i in range(x) for k in range(z) \
            for j in range(y)]
        dims = [x, z, y]
    else:
        S = [Mats[k][i][j] for k in range(z) for i in range(x) \
            for j in range(y)]
        dims = [z, x, y]
    return tuple(S), tuple(dims)


def _check_for_input_errors(M, a, b):
    # Check that a and b are integers
    if not _is_int(a):
        raise TypeError("'a' must be an integer")
    if not _is_int(b):
        raise TypeError("'b' must be an integer")
    # Now check that their values make sense
    if not a in {0, 1, 2}:
        raise ValueError("Expected 'a' to be in {0, 1, 2}.")
    if not b in {0, 1, 2}:
        raise ValueError("Expected 'b' to be in {0, 1, 2}.")
    if a == b:
        raise ValueError("'a' and 'b' must be distinct.")

    # Check that M is a sequence of matrices
    if not type(M) in {list, tuple}:
        raise TypeError("'M' must be a list or tuple of matrices.")
    if len(M) == 0:
        raise ValueError("'M' must be nonempty.")
    # Actually, I have no idea how to check if M is a list of mats...
    


def TensorFromArray(R, dims, S):
    # Check data makes sense
    if not type(S) in {list, tuple}:
        raise TypeError("'S' must be a list or tuple.")
    if len(S) != reduce(lambda x, y: x*y, dims, 1):
        raise ValueError("Dimensions and length of list do not match.")
    
    F = _FreeRFrame(R, dims)
    coerce = lambda x: R.coerce(x)
    S_R = tuple(map(coerce, S))
    multimap = _sequence_as_tensor(R, dims, S)
    return _Tensor(F, multimap, struct_consts = S)


def TensorFromMatrices(M, a, b):
    # Check to make sure input is reasonable
    _check_for_input_errors(M, a, b)

    # Transpose the matrix if not in expected order
    if a < b:
        fix = lambda x: _transpose(x)
    else:
        fix = lambda x: x

    # 'Matrix' is an idempotent function
    Mats = [fix(_Matrix(X)) for X in M]

    # Build sequences and dims and construct tensors
    S, dims = _matrices_to_sequence(Mats, a, b)
    R = Mats[0].base_ring()

    return TensorFromArray(R, dims, S)
