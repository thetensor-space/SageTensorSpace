#
#   Copyright 2019 Joshua Maglione and James B. Wilson
#
#   Distributed under MIT License
#

class Tensor:

    def __init__(self, frame, multimap, struct_consts=None):
        
        # TODO: How to check that frame is a TensorFrame???

        assert(isinstance(multimap, type(lambda x: x))), "multimap must be a function."
        self.map = multimap

        if not struct_consts is None:
            self.grid = struct_consts
    
    def __repr__(self):

        valence = len(self.dims)
        s = "Tensor of valence %s over %s.\n" % (valence, self.ring)

        if valence >= 3:
            for i in range(valence-1, 1, -1):
                s += "U" + str(i) + " x "

        if valence >= 2:
            s += "U1 >-> U0\n"
        else:
            s += "U0\n"
        
        mod_str = lambda x, y : str(FreeModule(x, y))

        return s[:-1]


