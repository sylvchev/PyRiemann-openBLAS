"""Covariance and utility class"""

# Authors: Sylvain Chevallier <sylvain.chevallier@uvsq.fr>
#          Romain Da Rocha <romain.da-rocha@isty.uvsq.fr>
#
# License: GNU GPL v3.0
from .CovMat import Covariance_Matrix
from .CovMats import Covariance_Matrices
from .estimation import estimate_covariances, estimate_covariances_EP
from .mean import Mean
# from .mean import (mean_riemann, mean_logeuclid, mean_logdet, mean_wasserstein,
#                    mean_euclid, mean_ale, mean_identity, mean_covariance
