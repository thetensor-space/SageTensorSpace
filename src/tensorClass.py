#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from frameClass import TensorFrame as _TensorFrame
from globalVars import _FUNCTION


def _print_tensor_exp(v):
    dom = reduce(lambda x, y: x + "U%s x " % (y), range(v-1, 0, -1), "")
    arrow = ">-> "
    if v > 1:
        return dom[:-2] + arrow + "U0\n"
    else:
        return "U0\n"


def _tensor_map_sanity(t):
    x = tuple([U.zero() for U in t.domain()])
    # Attempt to evalute all zeros using the multimap given
    y = t._map(x)

    # Check that the output makes sense
    if not y in t.codomain():
        raise TypeError("Tensor image outside of codomain.")
    if y != t.codomain().zero(): 
        raise ValueError("Tensor map is not multilinear.")
    


class Tensor():

    def __init__(self, frame, multimap, struct_consts=None):
        
        # Check that frame is a TensorFrame
        if not isinstance(frame, _TensorFrame):
            raise TypeError("'frame' must be an instance of TensorFrame.")
        self._frame = frame

        # Check multimap is a function
        if not isinstance(multimap, _FUNCTION): 
            raise TypeError("'multimap' must be a function.")
        self._map = multimap

        self._grid = struct_consts

        # Check the multimap makes sense
        _tensor_map_sanity(self)

    
    def __add__(self, other):
        added = lambda x: self(x) + other(x)
        return Tensor(self._frame, added)

    
    # Not crazy about this notation: t(x)
    def __call__(self, x):
        return self._map(x)


    def __repr__(self):

        F = self._frame
        v = F.valence()

        # Build the strings
        first_part = "Tensor of valence %s, " % (v)
        second_part = _print_tensor_exp(v)
        frame_lines = str(F)[str(F).index("\n")+1:]

        return first_part + second_part + frame_lines


    def base_ring(self):
        return self.frame().base_ring()

    def codomain(self):
        return self.frame().modules()[-1]

    def domain(self):
        return tuple(self.frame().modules()[:-1])

    def frame(self):
        return self._frame

    def valence(self):
        return self.frame().valence()