# Utility functions for processing .csv data in assignment 6

# get_files function:
import os
import glob
import natsort
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_files(pattern):
    """ get list of files from file data  pattern

    """
    if isinstance(pattern,list):
        pattern = os.path.join(*pattern)
    files = natsort.natsorted(glob.glob(pattern))
    return files


def find_middle(in_column):
    """ find middle of column and return index

    """
    middle = float(len(in_column))/2
    return int(np.floor(middle))

def realign_data(in_data, align):
    """ Center data around max or center of shortest column
    Args:
        in_data: array of input data
        align (str): "max" or "center"

    Returns:
        d - new data frame
        shifts - how each column is shifted
    """
    x, y = in_data.shape
    d = pd.DataFrame(0, index=np.arange(x), columns = np.arange(y))
    shifts = np.zeros(y)

    #Find longest lenght
    ind_longest = np.argmin((in_data == 0).astype(int).sum(axis=0))
    peak_longest = np.argmax(in_data.loc[:, ind_longest].values)
    # use your find_middle function here to find the center point for the assignment
    mid_longest = find_middle(in_data.index[in_data[ind_longest]!=0].values)

    # arrange the rest of the data's peaks into the new dataframe lining up to longest peak or longest midpoint
    for column in in_data:
        if align == "max":
            peak = np.argmax(in_data[column].values)
            pdiff = peak_longest - peak
            d[column] = in_data[column].shift(periods=pdiff, fill_value=0)
            # check shifted max location of input is same as reference peak
            #assert np.argmax(d[column]) == peak_longest
            shifts[column] = pdiff
        elif align == "center":
            # Write the alignment code here, replacing peak with the center that you found (mid_longest).
            middle = find_middle(in_data.index[in_data[column]!=0].values)
            mdiff = mid_longest - middle
            d[column] = in_data[column].shift(periods=mdiff, fill_value=0)
            shifts[column] = mdiff
    return d, shifts
