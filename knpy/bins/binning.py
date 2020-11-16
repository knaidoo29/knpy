import numpy as np



def bin_data(data, minimum=None, maximum=None, bin_size=None, bin_number=100,
             normalised=False, epsilon=1e-6):
    """Returns the number count of a data set with values within defined bins.

    Parameters
    ----------
    data : array
        The data to be binned.
    minimum : float, optional
        A given minimum for the bin edges.
    maximum : float, optional
        A given maximum for the bin edges
    bin_size : float, optional
        The size of the bins.
    bin_number : int, optional
        The number of bins to be used.
    normalised : bool
        If true will return a normalised histogram, if false returns a number counts.
    epsilon : float
        Fractional shift in calculated minimum and maximums.

    Returns
    -------
    bin_centers : array
        The central value of each bin.
    binned_data : array
        The binned number count (or normalised histogram) of the data set.
    """
    if minimum is None and maximum is None:
        minimum = data.min()
        maximum = data.max()
        minimum -= epsilon*(maximum - minimum)
        maximum += epsilon*(maximum - minimum)
    elif minimum is None:
        minimum = data.min()
        minimum -= epsilon*(maximum - minimum)
    elif maximum is None:
        maximum = data.max()
        maximum += epsilon*(maximum - minimum)
    if bin_size is None:
        bin_edge = np.linspace(minimum, maximum, bin_number+1)
    else:
        bin_edge = np.arange(minimum, maximum+bin_size, bin_size)
    binned_data, bin_edges = np.histogram(data, bins=bin_edge, normed=normalised)
    bin_centres = 0.5 * (bin_edge[1:] + bin_edge[:-1])
    binned_data = binned_data.astype('float')
    return bin_centres, binned_data


def edges2centers(bin_edges):
    """Returns the centers of bins of uniformly spaced bins.

    Parameters
    ----------
    bin_edges : array
        The midpoint of each bin.

    Returns
    -------
    bin_centres : array
        The edges of each bin.
    """
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    return bin_centers


def centers2edges(bin_centers):
    """Returns the bin edges of uniformly spaced bins.

    Parameters
    ----------
    bin_centers : array
        The midpoint of each bin.

    Returns
    -------
    bin_edges : array
        The edges of each bin.
    """
    dx = bin_centers[1] - bin_centers[0]
    bin_edges = np.ones(len(bin_centers) + 1)
    bin_edges[:-1] = bin_centers - dx/2.
    bin_edges[-1] = bin_centers[-1] + dx/2.
    return bin_edges


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
