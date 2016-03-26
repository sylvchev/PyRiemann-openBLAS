"""Optimized version of the Alexandre Barachant toolbox"""

# Authors: Sylvain Chevallier <sylvain.chevallier@uvsq.fr>
#          Romain Da Rocha <romain.da-rocha@isty.uvsq.fr>
#
# License: GNU GPL v3.0

from .covariances import Covariances
from spatialfilters import Xdawn
from .utils.CovMat import Covariance_Matrix
from .utils.CovMats import Covariance_Matrices
from .utils.estimation import estimate_covariances
