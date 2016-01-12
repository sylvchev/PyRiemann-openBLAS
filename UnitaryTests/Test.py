import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# test cases (nose)

# Base test cases

from UnitaryTests.Base.Expm import test_expm
from UnitaryTests.Base.Sqrtm import test_sqrtm
from UnitaryTests.Base.Logm import test_logm
from UnitaryTests.Base.Powm import test_powm
from UnitaryTests.Base.Invsqrtm import test_invsqrtm

# Distance test cases

from UnitaryTests.Distance.Kullback import test_distance_kullback, test_distance_kullback_right, test_distance_kullback_sym
from UnitaryTests.Distance.Euclidean import test_euclidean
from UnitaryTests.Distance.Log import test_distance_logdet, test_log_euclidean

# Geodesic test cases



# Mean



# end of test cases
"""
if test_expm():
    print("Test expm : Passed")
else:
    print("Test expm : Failed")
"""





