#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#

from sage.modules.free_module import FreeModule_ambient_field as _vec
from sage.modules.free_module import FreeModule_ambient_domain as _mod
from sage.rings.ring import Ring as _rng
from sage.rings.integer import Integer as _int

_VECTOR_SPACE = _vec
_FREE_MODULE = _mod
_FUNCTION = type(lambda x: x)
_RING = _rng
_INTEGER = _int