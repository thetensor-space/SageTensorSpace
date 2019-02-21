#
#   Copyright 2019 Joshua Maglione
#
#   Distributed under MIT License
#


# Given the dimensions of the domain spaces, dims, and a tuple of integers 
# corresponding to basis vectors, curr, return the "next" tuple by adding one 
# in the smallest coordinate. 
# TYPE: (dims: tuple[Integer], curr: tuple[Integer]): tuple[Integer]
def _next_gen(dims, curr):
    n = len(dims)
    zipped = zip(dims, curr)
    check = map(lambda x: x[0] == x[1], zipped)
    if all(check):
        return tuple([0 for i in dims])
    else:
        k = len(check) - check[::-1].index(False) - 1
        new = list(curr[:k]) + [curr[k] + 1] + [1 for i in range(k+1, n)]
        return tuple(new)


# Given the tuple of domain spaces, dom, and a tuple of integers x, return the 
# tuple of basis vectors whose index is given by x. 
# TYPE: (dom: tuple[_MOD], x: tuple[Integer]): tuple[tuple]
def _get_basis_tuple(dom, x):
    bases = [X.basis() for X in dom]
    tup = zip(x, bases)
    return tuple([T[1][T[0] - 1] for T in tup])


# Probably not stack safe, but it is functional!
# TYPE: (t: Tensor, dims: tuple[Integer], curr: tuple[Integer], 
#   struct_consts: list[tuple]): list[tuple]
# def _build_struct_consts(t, dims, curr, struct_consts):
#     if all(map(lambda x: x == 0, curr)):
#         return struct_consts
#     else:
#         new = struct_consts + [_get_basis_tuple(t.domain(), curr) * t]
#         return _build_struct_consts(t, _next_gen(dims, curr), new)


# Not functional, but better for Python.
# TYPE: (t: Tensor, dims: tuple[Integer]): list[tuple]
def _build_struct_consts(t, dims):
    curr = tuple([1 for i in dims])
    struct_consts = []
    while curr[0] != 0:
        struct_consts += list(t(_get_basis_tuple(t.domain(), curr)))
        curr = _next_gen(dims, curr) 
    return tuple(struct_consts)



def StructureConstants(t):
    if t._grid != None:
        return t._grid
    dims_dom = t.frame().dimensions()[:-1]
    t._grid = _build_struct_consts(t, dims_dom)
    return t._grid