import numpy as np


def rebin(x, y, numbins):
    """Rebins a binned data vector y.

    Parameters
    ----------
    x : array
        X coordinate centers for bins.
    y : array
        Bin heights.
    numbins : int
        Desired number of bins.

    Returns
    -------
    x_rebin : array
        Rebinned bin centers.
    y_rebin : array
        Rebinned bin heights.
    """
    assert len(x) % numbins == 0, "numbins has to be a factor of len(x)"
    x_rebin = np.mean(x.reshape(int(len(x)/numbins), int(numbins)), axis=1)
    y_rebin = np.sum(y.reshape(int(len(x)/numbins), int(numbins)), axis=1)
    return x_rebin, y_rebin
