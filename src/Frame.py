#
#   Copyright 2019 Joshua Maglione and James B. Wilson
#
#   Distributed under MIT License
#

from functools import reduce


# Given a list of a bases of free modules, determine if they have the same base
# ring.
def _check_consistent_ring(mods):
    vecs_flat = reduce(lambda x, y: x + y, mods)
    get_ring = lambda x: parent(x).base_ring()
    rings = map(get_ring, vecs_flat)
    same = all(map(lambda x: x == rings[0], rings[1:]))
    return same


class TensorFrame:

    def __init__(self, bases):

        print(type(bases))

        assert type(bases) in {list, tuple}, "bases must be a list/ tuple."
        assert len(bases) > 0, "Number of modules must be positive."
        assert _check_consistent_ring(bases), "Modules must have the same base ring."
        
        R = parent(bases[0]).base_ring()
        self.ring = R
