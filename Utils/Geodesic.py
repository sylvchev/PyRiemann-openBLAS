import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Geodesic(object):
    @staticmethod
    def euclidean(covmat1, covmat2, alpha=0.5):
        return (1 - alpha) * covmat1 + alpha * covmat2

    @staticmethod
    def log_euclidean(covmat1, covmat2, alpha=0.5):
        return ((1 - alpha) * covmat1.logm + alpha * covmat2.logm).expm

    @staticmethod
    def riemannian(covmat1, covmat2, alpha=0.5):
        return covmat1.sqrtm * (covmat1.invsqrtm * covmat2 * covmat1.invsqrtm).powm(alpha) * covmat1.sqrtm
