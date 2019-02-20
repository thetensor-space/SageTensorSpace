#
#   Copyright 2019 Joshua Maglione and James B. Wilson
#
#   Distributed under MIT License
#

def _print_tensor_exp(v):
    dom = reduce(lambda x, y: x + "U%s x " % (y), range(v, 0, -1))



class Tensor:

    def __init__(self, frame, multimap, struct_consts=None):
        
        # TODO: How to check that frame is a TensorFrame???
        self._frame = frame

        assert(isinstance(multimap, type(lambda x: x))), "multimap must be a function."
        self._map = multimap

        if not struct_consts is None:
            self._grid = struct_consts
    
    def __repr__(self):

        valence = len(self.dims)
        first_line = "Tensor of valence %s over %s.\n" % (valence, self.ring)

        mod_str = lambda x, y : str(FreeModule(x, y))

        return s[:-1]


