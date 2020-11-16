import numpy as np


def divide_1D(x, divisions, ranges=None, epsilon=1e-6):
    """Returns division indexes for x.

    Parameters
    ----------
    x : array
        Dataset used to divide the data.
    divisions : int
        Number of divisions to use.
    ranges : list
        Ranges of the dataset.
    epsilon : float
        Fractional shift in calculated minimum and maximums.

    Returns
    -------
    index : array
        Division indexes. Out of range assigned index = -1.
    """
    # check minimum and maximum definitions
    if ranges is None:
        xmin = x.min()
        xmax = x.max()
    else:
        if ranges[0] is None:
            xmin = x.min()
        else:
            xmin = ranges[0]
        if ranges[1] is None:
            xmax = x.max()
        else:
            xmax = ranges[1]
    x_range = xmax - xmin
    xmin -= x_range*epsilon
    xmax += x_range*epsilon
    # calculate division widths
    dx = xmax - xmin
    dx /= divisions
    # calculate indexes
    index = np.floor((x - xmin)/dx)
    condition = np.where(index > divisions)[0]
    index[condition] = -1
    return index


def divide_ND(pos, divisions, ranges=None):
    """Returns division indexes for pos.

    Parameters
    ----------
    pos : list
        A list of the datasets used to divide the data.
    divisions : int
        Number of divisions to use along each axis.
    ranges : list
        Ranges of the dataset.

    Returns
    -------
    index : array
        Division indexes. Out of range assigned index = -1.
    """
    if ranges is None:
        ranges = [None for i in range(0, len(pos))]
    else:
        len(pos) == len(ranges), "Number of axes must match for pos and ranges."
    indexes = [divide_1D(pos[i], divisions, ranges=ranges[i]) for i in range(0, len(pos))]
    for i in range(0, len(indexes)):
        if i == 0:
            index = indexes[i]
        else:
            index *= divisions
            index += indexes[i]
    return index
