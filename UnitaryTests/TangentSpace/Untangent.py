import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from Utils.CovMats import CovMats, CovMat

from oldPyRiemann.tangentspace import untangent_space
from Utils.TangentSpace import TangentSpace

def test_untangent():
    covmat = CovMat.random(10)
    covmats = CovMats.random(10, 10)
    tangent = TangentSpace.tangent(covmats, covmat)
    old = untangent_space(tangent, covmat.numpy_array)
    covmats.reset_covmats_fields()
    new = TangentSpace.untangent(tangent, covmat)

    return _get_state(old, new, "untangent")

def _get_state(old, new, func_name):
    if abs( old.sum() - new.sum() ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False