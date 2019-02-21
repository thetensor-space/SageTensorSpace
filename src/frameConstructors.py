#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from sage.all import parent as _parent
from sage.all import FreeModule as _FreeModule
from frameClass import _build_modules
from frameClass import TensorFrame as _TensorFrame
from globalVars import _FREE_MODULE, _is_int, _RING


def _Construct_mod(X):
    # I am just going to assume if X is a list/tuple, then it is a basis for 
    # some submodule.
    if not type(X) in {list, tuple}:
        if not isinstance(X, _FREE_MODULE):
            raise TypeError("Argument is not a basis nor a free module over a domain.")
        return X.basis()


# Given a list or tuple, L, of R-modules, return the corresponding tensor 
# frame such that L[0] is the 0th coordinate. 
def FrameFromList(L, left = True):
    if not type(L) in {list, tuple}:
        raise TypeError("Argument must be a list or tuple.")
    bases = map(_Construct_mod, L)
    return _TensorFrame(bases, left_just = left)


def FreeRFrame(R, dims, left = True):
    # Lots of error checking because no typing
    if not isinstance(R, _RING):
        raise TypeError("'R' must be a ring.")
    if not type(dims) in {list, tuple}:
        raise TypeError("'dims' must be a list or tuple of nonnegative integers.")

    int_and_pos = lambda x: _is_int(x) and x >= 0
    if not all(map(int_and_pos, dims)):
        raise TypeError("'dims' must be a list or tuple of nonnegative integers.")

    return FrameFromList([_FreeModule(R, d) for d in dims], left = left)