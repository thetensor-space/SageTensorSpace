#
#   Copyright 2019 Joshua Maglione 
#
#   Distributed under MIT License
#


class TensorSpace():

    def __init__(self, frame, basis):
        
        # Check that frame is a TensorFrame
        if not isinstance(frame, _TensorFrame):
            raise TypeError("'frame' must be an instance of TensorFrame.")
        self._frame = frame

        self._basis = basis