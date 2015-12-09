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



# Geodesic test cases



# end of test cases
"""
if test_expm():
    print("Test expm : Passed")
else:
    print("Test expm : Failed")
"""





