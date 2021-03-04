import numpy as np


def get_binmask(mask):
    """Returns a binary mask from a float mask.

    Parameters
    ----------
    mask : array
        Float mask.

    Returns
    -------
    binmask : array
        Binary mask.
    """
    binmask = np.zeros(len(mask))
    condition = np.where(mask != 0.)[0]
    binmask[condition] = 1.
    return binmask


def binmask2index(binmask):
    """Returns index in a binary mask.

    Parameters
    ----------
    binmask : array
        Binary mask.

    Returns
    -------
    mask_ind : array
        Index in the mask.
    """
    mask_ind = np.where(binmask == 1.)[0]
    return mask_ind


def index2binmask(mask_ind, masklen):
    """Creates a binary mask from the mask indexes.

    Parameters
    ----------
    mask_ind : array
        Index in the mask.
    mask_len : int
        Length of the original array and mask.

    Returns
    -------
    binmask : array
        Binary mask.
    """
    binmask = np.zeros(masklen)
    binmask[mask_ind] = 1.
    return binmask


def remove_masked(data, binmask):
    """Fills a masked data values.

    Parameters
    ----------
    data : array
        Data array.
    binmask : array
        Binary mask.

    Returns
    -------
    mask_data : array
        Masked data.
    """
    mask_ind = ind_in_mask(binmask)
    mask_data = data[mask_ind]
    return mask_data


def fill_masked(mask_data, mask_ind, mask_len, fill_value=0.):
    """Fills a masked data values.

    Parameters
    ----------
    mask_data : array
        Masked data.
    mask_ind : array
        Index in the mask.
    mask_len : int
        Length of the original array and mask.
    fill_value : float, optional
        Value to fill the array.

    Returns
    -------
    data : array
        A new array constructed with filled values.
    """
    data = np.ones(mask_len) * fill_value
    data[mask_ind] = mask_data
    return data
