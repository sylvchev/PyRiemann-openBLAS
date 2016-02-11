import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# test cases (nose)

# Base test cases
"""
"""
from UnitaryTests.Base.Expm import test_expm
from UnitaryTests.Base.Sqrtm import test_sqrtm
from UnitaryTests.Base.Logm import test_logm
from UnitaryTests.Base.Powm import test_powm
from UnitaryTests.Base.Invsqrtm import test_invsqrtm

# Distance test cases

from UnitaryTests.Distance.Kullback import test_distance_kullback, test_distance_kullback_right, test_distance_kullback_sym
from UnitaryTests.Distance.Euclidean import test_euclidean
from UnitaryTests.Distance.Log import test_log_euclidean, test_distance_logdet
from UnitaryTests.Distance.Riemmanian import test_distance_riemman
from UnitaryTests.Distance.Wasserstein import test_distance_wasserstein

# Geodesic test cases

from UnitaryTests.Geodesic.Riemannian import test_geodesic_riemann
from UnitaryTests.Geodesic.Euclidean import test_geodesic_euclidean
from UnitaryTests.Geodesic.LogEuclidean import test_geodesic_log_euclidean

# Mean

from UnitaryTests.Mean.Euclidean import test_mean_euclidean
from UnitaryTests.Mean.Log import test_mean_log_determinant, test_mean_log_euclidean
from UnitaryTests.Mean.Riemann import test_mean_riemann
from UnitaryTests.Mean.Wasserstein import test_mean_wasserstein

# Tangent Space test cases

from UnitaryTests.TangentSpace.Tangent import test_tangent
from UnitaryTests.TangentSpace.Untangent import test_untangent

# end of test cases
"""
if test_expm():
    print("Test expm : Passed")
else:
    print("Test expm : Failed")
"""