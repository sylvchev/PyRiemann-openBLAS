import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from Utils.CovMats import CovMats
from Utils.CovMat import CovMat
from Utils.Mean import Mean
from Utils.Geodesic import Geodesic

from oldPyRiemann.tangentspace import tangent_space
from Utils.TangentSpace import TangentSpace

def test_tangent():
    covmat = CovMat.random(10)
    covmats = CovMats.random(10, 10)
    old = tangent_space(covmats.numpy_array, covmat.numpy_array)
    covmats.reset_covmats_fields()
    new = TangentSpace.tangent(covmats, covmat)

    return _get_state(old, new, "tangent space")

def _get_state(old, new, func_name):
    if abs( old.sum() - new.sum() ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False