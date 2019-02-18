#
#   Copyright 2019 Joshua Maglione
#
#   Distributed under MIT License
#

class Tensor:

    def __init__(self, basering, frame, multimap, struct_consts=None):
        
        self.ring = basering
        
        assert(isinstance(frame, tuple) or isinstance(frame, list)), "Frame must be given as a tuple or list."
        assert(all(map(lambda x: isinstance(x, type(0)) and (x >= 0), frame))), "Frame tuple must contain nonnegative integers."
        self.dims = frame

        assert(isinstance(multimap, type(lambda x: x))), "multimap must be a function."
        self.map = multimap

        if not(struct_consts is None):
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

        for i in range(valence):
            s += "U" + str(valence - i - 1) + " : " + mod_str(self.ring, self.dims[i]) + "\n"

        return s[:-1]


