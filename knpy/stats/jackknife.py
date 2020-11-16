import numpy as np

from .. import utils


class Jackknife:
    """Class for Jackknife resampling."""


    def __init__(self):
        """Initialises the class."""
        self.stat_func = None
        self.stat_args = None
        #self.stat_args_full = None
        self.jack_index = None
        self.unique_jack = None
        self.jack_Nsamples = None
        self.jackknife_samples = None


    def setup(self, stat_func, stat_args, jack_index):#, stat_args_full=None):
        """Sets up the Jackknife resampling.

        Parameters
        ----------
        stat_func : function
            The statistical function of interest.
        stat_args : list
            additional arguments for the statistical function.
        jack_index : array
            Division indexes. Out of range assigned index = -1.
        """
        self.stat_func = stat_func
        self.stat_args = stat_args
        # if stat_args_full is None:
        #     self.stat_args_full = stat_args
        # else:
        #     self.stat_args_full = stat_args_full
        self.jack_index = jack_index
        self.jack_unique_index = np.unique(jack_index)
        if self.jack_unique_index[0] == -1:
            self.jack_unique_index = self.jack_unique_index[1:]
        self.jack_Nsamples = len(self.jack_unique_index)


    def run(self, verbose=True):
        """Calculates Jackknife resampling statistics.

        Parameters
        ----------
        verbose : bool
            Prints what is being calculated.

        Returns
        -------
        jack_mean : array
            Jackknife sample mean.
        jack_std : array
            Jackknife sample standard deviation.
        """
        self.jack_samples = []
        for i in range(0, len(self.jack_unique_index)):
            condition = np.where((self.jack_index != self.jack_unique_index[i]) &
                                 (self.jack_index != -1))[0]
            jack_sample = self.stat_func(condition, self.stat_args)
            self.jack_samples.append(jack_sample)
            if verbose == True:
                utils.progress_bar(i, len(self.jack_unique_index), explanation='Calculating Jackknife Samples')
        if verbose == True:
            print('Calculate Jackknife mean')
        self.jack_samples = np.array(self.jack_samples)
        self.jack_mean = np.mean(self.jack_samples, axis=0)
        #if verbose == True:
        #    print('Jackknife mean bias correction')
        # bias correction
        #self.nojack_sample = self.stat_func(np.arange(len(self.jack_samples)), self.stat_args_full)
        #self.jack_mean = self.nojack_sample - (float(self.jack_Nsamples) - 1.)*(self.jack_mean - self.nojack_sample)
        if verbose == True:
            print('Calculate Jackknife variance')
        # variance calculation
        jack_sq = np.array([(self.jack_samples[i] - self.jack_mean)**2. for i in range(0, len(self.jack_samples))])
        self.jack_var = ((float(self.jack_Nsamples)-1.)/float(self.jack_Nsamples))
        self.jack_var *= np.sum(jack_sq, axis=0)
        self.jack_std = np.sqrt(self.jack_var)
        return self.jack_mean, self.jack_std


    def clean(self):
        """Reinitialises the class and resets class parameters."""
        self.__init__()
