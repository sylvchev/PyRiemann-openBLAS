#!/usr/bin/python

import sys
import os
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "PyRiemann")))

import Utils.OpenBLAS as OpenBLAS

# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

data_type = None
memory_safe_state = None
nb_threads = None

with open("../config.cfg") as file:
    for line in file.readlines():
            words = line.split('=')

            if words[0] == "data_type":
                if words[1] == "double\n":
                    data_type = numpy.dtype('d')
                elif words[1] == "float\n":
                    data_type = numpy.dtype('f')
                elif words[1] == "integer\n":
                    data_type = numpy.dtype('i')
                else:
                    print("Error in data type while parsing config.cfg. Data type automatically set to double precision")
                    data_type = numpy.dtype('d')

            if words[0] == "memory_safe_state":
                if words[1] == "True\n" or words[1] == "true\n":
                    memory_safe_state = True
                elif words[1] == "False\n" or words[1] == "false\n":
                    memory_safe_state = True
                else:
                    print("Error in memory safe state while parsing config.cfg. memory safe state automatically set to True")
                    memory_safe_state = True

            if words[0] == "nb_threads":
                try:
                    nb_threads = int(words[1])
                except ValueError:
                    print("Error in number of threads while parsing config.cfg. Number of threads automatically set to the max possible")
                    nb_threads = OpenBLAS.get_nb_procs()

OpenBLAS.set_nb_threads(nb_threads)