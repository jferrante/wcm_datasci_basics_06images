import numpy as np
import pandas as pd
from ..functions.utils import find_middle
from ..functions.utils import realign_data

def test_find_middle_even():
    # test if even sized data array returns a mid 1/2 its size
    test_array = np.arrange(8)
    mid = 4
    output = find_middle(test_array)
    assert output == mid

def test_find_middle_odd():
    # test if odd sized data array returns a mid that is the
    # floor of 1/2 its size
    test_array = np.arrange(9)
    mid = 4
    output = find_middle(test_array)
    assert output == mid

def test_realign_max():

    assert
