#
#   Copyright 2019 Joshua Maglione and James B. Wilson
#
#   Distributed under MIT License
#

from sage.all import *
from functools import reduce as _reduce


# Given a list of a bases of free modules, determine if they have the same base
# ring.
def _check_consistent_ring(mods):
    vecs_flat = _reduce(lambda x, y: x + y, mods)
    get_ring = lambda x: parent(x).base_ring()
    rings = map(get_ring, vecs_flat)
    same = all(map(lambda x: x == rings[0], rings[1:]))
    return same

# Given a tuple of the form (module, basis), return the corresponding free
# submodule.
def _build_modules(zipped):
    if zipped[0].dimension() == len(zipped[1]):
        return zipped[0]
    else:
        return zipped[0].subspace(zipped[1])

# Given a tuple of the form (module, integer), a module and its coordinate,
# construct the print statement.
def _print_module(zipped):
    return "U" + str(zipped[1]) + " : " + str(zipped[0]) + "\n"




class TensorFrame:

    def __init__(self, bases):

        # Check that the data makes sense
        assert type(bases) in {list, tuple}, "bases must be a list/ tuple."
        assert len(bases) > 0, "Number of modules must be positive."
        assert _check_consistent_ring(bases), "Modules must have the same base ring."
        
        # Build necessary information
        spaces = map(lambda x: parent(x[0]), bases)
        mods = tuple(map(_build_modules, zip(spaces, bases)))

        # Store the information
        self._modules = mods


    def __repr__(self):
        
        # Zip the modules and their coordinates together.
        coords = range(self.valence() - 1, -1, -1)
        zipped = zip(self.modules(), coords)

        # Convert the tuples to strings and cat them together.
        list_of_str = map(_print_module, zipped)
        first = "Tensor frame of valence " + str(self.valence()) + ":\n"
        return first + reduce(lambda x, y: x + y, list_of_str)[:-1]


    def dimensions(self):
        return tuple(map(lambda x: x.dimension(), self._modules))

    def gen(self, a):
        # Seems as though Sage won't accept negatives by default.
        # assert a >= 0, "Coordinate must be nonnegative."
        assert a < self.valence(), "Coordinate is too large."
        return (self._modules)[-1 - a]

    def modules(self):
        return self._modules

    def ring(self):
        return (self._modules[0]).base_ring()

    def valence(self):
        return len(self._modules)

