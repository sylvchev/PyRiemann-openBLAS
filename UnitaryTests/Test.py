#!/usr/bin/python

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from UnitaryTests.Base.Expm import test_expm

if test_expm() :
    print("Test expm : Passed")
else :
    print("Test expm : Failed")