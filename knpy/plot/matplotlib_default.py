
def set_matplotlib_default():
    """Set default fonts and latex for matplotlib plots."""
    
    from matplotlib import rcParams, rc

    params = {
        'text.usetex': True,
        'font.family':'serif'}
    # use of Sans Serif also in math mode

    rc('text.latex', preamble=r'\usepackage{amsmath}')
    rcParams.update(params)
