#
#   Copyright 2019 Joshua Maglione
#
#   Distributed under MIT License
#

# I don't think this....
def _next_gen(dims):
    n = len(dims)
    curr = [1 for i in range(n-1)] + [0]
    while True

        zipped = zip(dims, curr)
        check = map(lambda x: x[0] == x[1], zipped)
        if all(check):
            raise GeneratorExit()
        else:
            k = len(check) - check[::-1].index(False) - 1
            curr = list(curr[:k]) + [curr[k] + 1] + [1 for i in range(k+1, n)]
            yield tuple(curr)


def _get_basis_tuple(dom, x):


def StructureConstants(t):
