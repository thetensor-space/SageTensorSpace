#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#


__version__ = 0.2

print("Loading...")

# === This is very annoying during development =================================
import sys
sys.dont_write_bytecode = True
# ==============================================================================

# 'from foo import *' leaves hidden functions hidden and brings it up to 
# TensorSpace instead of TensorSpace.src

# Frames 
from src.frameClass import *
from src.frameConstructors import *

# Tensors
from src.tensorClass import *
from src.tensorConstructors import *
from src.tensorStructureConstants import *

# Tensor Spaces
from src.tensorSpaceClass import *


# Sage is still on python2.
print "TensorSpace %s loaded." % (__version__)