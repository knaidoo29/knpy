import numpy as np
from scipy.optimize import minimize
import george


def neg_ln_like(p, y, gp):
    gp.set_parameter_vector(p)
    return -gp.log_likelihood(y)


def grad_neg_ln_like(p, y, gp):
    gp.set_parameter_vector(p)
    return -gp.grad_log_likelihood(y)


class GaussianProcesses:
    """Gaussian Process class for simple GP regression using george"""

    def __init__(self):
        """Initialises class."""
        self.x = None
        self.y = None
        self.yerr = None
        self.gp = None

    def optimize(self, x, y, yerr, verbose=False):
        """Gaussian Process hyperparameter optimisation.

        Parameters
        ----------
        x : array
            X-values.
        y : array
            Y-values.
        yerr : array
            Y-value errors.
        """
        condition = np.where((np.isfinite(yerr) == True) & (yerr != 0.))[0]
        self.x = x[condition]
        self.y = y[condition]
        self.yerr = yerr[condition]
        kernel = george.kernels.Matern32Kernel(1.)
        kernel *= np.var(self.y)
        self.gp = george.GP(kernel)
        self.gp.compute(self.x, self.yerr)
        result = minimize(neg_ln_like, self.gp.get_parameter_vector(), jac=grad_neg_ln_like, args=(self.y, self.gp))
        self.gp.set_parameter_vector(result.x)
        if verbose == True:
            print("\nFinal ln-likelihood: {0:.2f}".format(self.gp.log_likelihood(self.y)))

    def predict(self, x_pred):
        """Predicts values at x_pred.

        Parameters
        ----------
        x_pred : array
            X-values to predict GP regression.

        Returns
        -------
        y_pred : array
            Predicted Y-values
        y_pred_var : array
            Associated variance for the GP prediction.
        """
        y_pred, y_pred_var = self.gp.predict(self.y, x_pred, return_var=True)
        return y_pred, y_pred_var

    def clean(self):
        """Reinitialises class and resets parameters"""
        self.__init__()
