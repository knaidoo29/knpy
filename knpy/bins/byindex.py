import numpy as np

from . import byindexfast


def bin_by_index(indexes, bins, weights=None):
    """Bins weigths according to index. This would have to be done in a for loop
    in python so this is passed on to a fortran module to rapidly do in for loop.

    Parameters
    ----------
    indexes : array
        Integer array of the indexes of the bin.
    bins : array
        Bin array.
    weights : array, optional
        Weights to bin by, otherwise assumed to be just counts.

    Returns
    -------
    bins : array
        Weighted bins.
    """
    # ind_uniq, ind_count = np.unique(indexes, return_counts=True)
    # for i in range(0, len(ind_uniq)):
    #     bins[ind_uniq[i]] += ind_count[i]
    # return bins
    if weights is None:
        # assume only counts are wanted.
        weights = np.ones(len(indexes))
    binin = np.copy(bins)
    binout = byindexfast.bin_by_index(indexes, weights, len(binin), len(indexes))
    bins = bins + binout
    return bins
