

def round_up(number, sig_fig=3):
    """Rounds up a number to the given significant figures.

    Parameters
    ----------
    number : float
        An unrounded float.
    sig_fig : int, optional
        Significant figures to round the number to.
    """
    return float(('%.'+('%i' % sig_fig)+'g') % number)
