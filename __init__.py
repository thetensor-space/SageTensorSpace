#
#   Copyright 2019 Joshua Maglione and James B. Wilson
#
#   Distributed under MIT License
#

__version__ = 0.1

print("Loading...")

# This is very annoying during development. 
import sys
sys.dont_write_bytecode = True

import src

# Sage is still on python2.
print("TensorSpace " + str(__version__) + " loaded.")