#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from globalVars import _INTEGER
from frameConstructors import Frame as _Frame
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
    mult = lambda x, y: x*y
    add = lambda x, y: x + y
    offsets = [reduce(mult, dims[i+1:], 1) for i in range(v - 1)] + [1]

    # The actual eval function
    def F(x):
        vec = [0 for i in range(dims[-1])]
        curr = [1 for i in range(v-1)]
        for i in range(dims[-1]):
            while curr[0] != 0:
                ind = [j-1 for j in curr] + [i]
                entry = reduce(add, [z[0]*z[1] for z in zip(ind, offsets)], 1)
                consts = [x[j][curr[j]-1] for j in range(len(x))]
                vec[i] += reduce(mult, consts, S[entry])
                curr = _next_gen(dims[:-1], curr)
        return _vector(R, vec)
    return F


def TensorFromArray(R, dims, S):
    # Check data makes sense
    if not type(S) in {list, tuple}:
        raise TypeError("'S' must be a list or tuple.")
    F = _Frame(R, dims)
    multimap = _sequence_as_tensor(R, dims, S)
    return _Tensor(F, multimap, struct_consts = S)


def TensorFromMatrices(M, a, b):
    # Check that a and b are integers
    if not isinstance(a, _INTEGER):
        raise TypeError("'a' must be an integer")
    if not isinstance(b, _INTEGER):
        raise TypeError("'b' must be an integer")
    if not a in {0, 1, 2}:
        raise ################################################################### 

    # Check that M is a sequence of matrices
    if not type(M) in {list, tuple}:
        raise TypeError("'M' must be a list or tuple of matrices.")
    # Actually, I have no idea how to check if M is a list of mats...
    
    if a < b then 
        fix = lambda x: _transpose(x)
    else:
        fix = lambda x: x
    # 'Matrix' is an idempotent
    Mats = [fix(_Matrix(X)) for X in M]

    if {a, b} == {1, 2}:

    elif {a, b} == {0, 2}:

    elif ###################################################################
