"""Mean covariance estimation."""
import numpy as np

from .CovMat import Covariance_Matrix
from .CovMats import Covariance_Matrices

class Mean(object):
    @staticmethod
    def identity(covmats):
        """Return the identity matrix corresponding to the covmats sit size
    
        .. math::
                \mathbf{C} = \mathbf{I}_d

        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :returns: the identity matrix of size Nchannels
        """
        return Covariance_Matrix.identity(covmats.dim)

    @staticmethod
    def euclidean(covmats, sample_weight=None):
        """Return the mean covariance matrix according to the euclidean metric :

        .. math::
                \mathbf{C} = \\frac{1}{N} \sum_i \mathbf{C}_i
    
        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :param sample_weight: the weight of each sample

        :returns: the mean covariance matrix
        """
        return Covariance_Matrix(covmats.average(0, sample_weight), False)

    @staticmethod
    def log_euclidean(covmats, sample_weight=None):
        """Return the mean covariance matrix according to the log-euclidean metric.

        .. math::
                \mathbf{C} = \exp{(\\frac{1}{N} \sum_i \log{\mathbf{C}_i})}

        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :param sample_weight: the weight of each sample

        :returns: the mean covariance matrix
        """
        logm_covmats = Covariance_Matrices([covmat.logm for covmat in covmats], False)
        return Covariance_Matrix(logm_covmats.average(0, sample_weight), False).expm

    @staticmethod
    def log_determinant(covmats, tol=10e-5, max_iter=50,
                        init=None, sample_weight=None):
        """Return the mean covariance matrix according to the logdet metric.

        This is an iterative procedure where the update is:

        .. math::
                \mathbf{C} = \left(\sum_i \left( 0.5 \mathbf{C} + 0.5 \mathbf{C}_i \\right)^{-1} \\right)^{-1}

        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :param tol: the tolerance to stop the gradient descent
        :param maxiter: The maximum number of iteration, default 50
        :param init: A covariance matrix used to initialize the iterative procedure. If None the Arithmetic mean is used
        :param sample_weight: the weight of each sample

        :returns: the mean covariance matrix
        """
        if init is None:
            output = Covariance_Matrix(covmats.mean(0), False)
        else:
            output = init
        k = 0
        crit = np.finfo(np.double).max
        while crit > tol and k < max_iter:
            k += 1
            tmp = Covariance_Matrices([(0.5 * (covmat + output)).inverse
                                       for covmat in covmats], False)
            # TODO: verify if it is average or sum
            new_output = Covariance_Matrix(tmp.average(0, sample_weight), False).inverse
            crit = (new_output - output).norm(ord='fro')
            output = new_output
        return output

    @staticmethod
    def riemannian(covmats, tol=10e-9, max_iter=50,
                   init=None, sample_weight=None):
        """Return the mean covariance matrix according to the Riemannian metric.

        The procedure is similar to a gradient descent minimizing the sum of
        riemannian distance to the mean.
    
        .. math::
                \mathbf{C} = \\arg\min{(\sum_i \delta_R ( \mathbf{C} , \mathbf{C}_i)^2)}

        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :param tol: the tolerance to stop the gradient descent
        :param maxiter: The maximum number of iteration, default 50
        :param init: A covariance matrix used to initialize the gradient descent. If None the Arithmetic mean is used
        :param sample_weight: the weight of each sample
        :returns: the mean covariance matrix
        """
        if init is None:
            output = Covariance_Matrix(covmats.mean(0), False)
        else:
            output = init
        k = 0
        nu = 1.0
        tau = np.finfo(np.double).max
        crit = np.finfo(np.double).max

        while crit > tol and k < max_iter and nu > tol:
            k += 1
            tmp = Covariance_Matrices([(output.invsqrtm*covmat*output.invsqrtm).logm
                                       for covmat in covmats], False)
            # TODO: idem average or sum?
            average = Covariance_Matrix(tmp.average(0, sample_weight), False)
            crit = average.norm(ord='fro')
            h = nu * crit
            output = output.sqrtm * (nu * average).expm * output.sqrtm
            if h < tau:
                nu *= 0.95
                tau = h
            else:
                nu *= 0.5
        return output
        
    @staticmethod
    def wasserstein(covmats, tol=10e-4, max_iter=1,
                    init=None, sample_weight=None):
        """Return the mean covariance matrix according to the wasserstein metric.

        This is an iterative procedure where the update is [1]:

        .. math::
                \mathbf{K} = \left(\sum_i \left( \mathbf{K} \mathbf{C}_i \mathbf{K} \\right)^{1/2} \\right)^{1/2}

        with :math:`\mathbf{K} = \mathbf{C}^{1/2}`.

        :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
        :param tol: the tolerance to stop the gradient descent
        :param maxiter: The maximum number of iteration, default 50
        :param init: A covariance matrix used to initialize the iterative procedure. If None the Arithmetic mean is used
        :param sample_weight: the weight of each sample
    
        :returns: the mean covariance matrix

        References
        ----------
        [1] Barbaresco, F. "Geometric Radar Processing based on Frechet distance:
        Information geometry versus Optimal Transport Theory", Radar Symposium
        (IRS), 2011 Proceedings International.
        """
        if init is None:
            output = Covariance_Matrix(covmats.mean(0))
        else:
            output = init
        k = 0
        crit = np.finfo(np.double).max

        while crit > tol and k < max_iter:
            k += 1
            tmp = Covariance_Matrices([(output.sqrtm*covmat*output.sqrtm).sqrtm
                                       for covmat in covmats], False)
            # TODO: idem, sum or average?
            average = Covariance_Matrix(tmp.average(0, sample_weight), False)

            new_output = average.sqrtm
            crit = (new_output - output.sqrtm).norm(ord='fro')
            output = new_output
        return output * output

# from numpy import finfo, ones, zeros
# from .base import sqrtm, invsqrtm, logm, expm
# from .ajd import ajd_pham
# from .distance import distance_riemann

# def _get_sample_weight(sample_weight, data):
#     """Get the sample weights.

#     If none provided, weights init to 1. otherwise, weights are normalized.
#     """
#     if sample_weight is None:
#         sample_weight = ones(data.shape[0])
#     if len(sample_weight) != data.shape[0]:
#         raise ValueError("len of sample_weight must be equal to len of data.")
#     sample_weight /= sample_weight.sum()
#     return sample_weight


# def mean_ale(covmats, tol=10e-7, maxiter=50, sample_weight=None):
#     """Return the mean covariance matrix according using the AJD-based
#     log-Euclidean Mean (ALE). See [1].

#     :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
#     :param tol: the tolerance to stop the gradient descent
#     :param maxiter: The maximum number of iteration, default 50
#     :param sample_weight: the weight of each sample

#     :returns: the mean covariance matrix

#     Notes
#     -----
#     .. versionadded:: 0.2.4

#     References
#     ----------
#     [1] M. Congedo, B. Afsari, A. Barachant, M. Moakher, 'Approximate Joint
#     Diagonalization and Geometric Mean of Symmetric Positive Definite
#     Matrices', PLoS ONE, 2015

#     """
#     sample_weight = _get_sample_weight(sample_weight, covmats)
#     Nt, Ne, Ne = covmats.shape
#     crit = numpy.inf
#     k = 0

#     # init with AJD
#     B, _ = ajd_pham(covmats)
#     while (crit > tol) and (k < maxiter):
#         k += 1
#         J = numpy.zeros((Ne, Ne))

#         for index, Ci in enumerate(covmats):
#             tmp = logm(numpy.dot(numpy.dot(B.T, Ci), B))
#             J += sample_weight[index] * tmp

#         update = numpy.diag(numpy.diag(expm(J)))
#         B = numpy.dot(B, invsqrtm(update))

#         crit = distance_riemann(numpy.eye(Ne), update)

#     A = numpy.linalg.inv(B)

#     J = numpy.zeros((Ne, Ne))
#     for index, Ci in enumerate(covmats):
#         tmp = logm(numpy.dot(numpy.dot(B.T, Ci), B))
#         J += sample_weight[index] * tmp

#     C = numpy.dot(numpy.dot(A.T, expm(J)), A)
#     return C




def mean_covariance(covmats, metric='riemann', sample_weight=None, *args):
    """Return the mean covariance matrix according to the metric


    :param covmats: Covariance matrices set, Ntrials X Nchannels X Nchannels
    :param metric: the metric (Default value 'riemann'), can be : 'riemann' , 'logeuclid' , 'euclid' , 'logdet', 'indentity', 'wasserstein'
    :param sample_weight: the weight of each sample
    :param args: the argument passed to the sub function
    :returns: the mean covariance matrix

    """
    options = {'riemann': mean_riemann,
               'logeuclid': mean_logeuclid,
               'euclid': mean_euclid,
               'identity': mean_identity,
               'logdet': mean_logdet,
               'wasserstein': mean_wasserstein,
               'ale': mean_ale}
    C = options[metric](covmats, sample_weight=sample_weight, *args)
    return C
