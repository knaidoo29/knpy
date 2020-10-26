
class FigureSize:

    def __init__(self):
        """Initialise class."""
        self.x_size = 8. #inches
        self.y_size = None
        self.ft = 12

    def get_size(self, x_ratio, y_ratio, mode='fullpage'):
        """Returns the size of the figure.

        Parameters
        ----------
        x_ratio : float
            The figure's x-axis ratio.
        y_ratio : float
            The figure's y-axis ratio.
        mode : str
            - 'fullpage': full page plots meaning the x-axis extends across the
            page in portrait format.
            - 'halfpage': half page plots to cover one column of 2 column paper.
        """
        if mode=='fullpage':
            x_size = self.x_size
        elif mode == 'halfpage':
            x_size = self.x_size/2.
        y_size = x_size*(y_ratio/x_ratio)
        return x_size, y_size

    def get_colorbar_thickness(self, x_ratio, y_ratio, thickness=0.096, mode='fullpage',
                               orientation='horizontal'):
        """Returns the thickness of a colorbar to ensure that colorbar thickness
        is kept uniform in all plots.

        Parameters
        ----------
        x_ratio : float
            The figure's x-axis ratio.
        y_ratio : float
            The figure's y-axis ratio.
        mode : str
            - 'fullpage': full page plots meaning the x-axis extends across the
            page in portrait format.
            - 'halfpage': half page plots to cover one column of 2 column paper.
        """
        x_size, y_size = self.get_size(x_ratio, y_ratio, mode=mode)
        if orientation == 'horizontal':
            return thickness / y_size
        else:
            return thickness / x_size

    def clean(self):
        """Reinitialises and resets parameter values."""
        self.__init__()
