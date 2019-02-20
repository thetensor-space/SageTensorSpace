#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from sage.all import parent as _parent
from frameClass import _build_modules
from frameClass import TensorFrame as _TensorFrame
from globalVars import _FREE_MODULE


def _Construct_mod(X):
    if not type(X) in {list, tuple}:
        assert isinstance(X, _FREE_MODULE), \
            "Argument is not a basis nor a free module over a domain."
        return X.basis()


# Given a list or tuple, L, of R-modules, return the corresponding tensor 
# frame such that L[0] is the 0th coordinate. 
def Frame(L, right = True):
    assert type(L) in {list, tuple}, "Argument must be a list or tuple."
    bases = map(_Construct_mod, L)
    return _TensorFrame(bases, right_just = right)
