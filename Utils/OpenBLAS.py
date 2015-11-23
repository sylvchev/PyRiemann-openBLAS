# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

# solution found here :
# http://stackoverflow.com/questions/29559338/set-max-number-of-threads-at-runtime-on-numpy-openblas
# Thanks to : ali_m

import ctypes
import os

openblas_lib = ctypes.cdll.LoadLibrary('/usr/local/lib/libopenblas.so')


def get_nb_threads():
    return openblas_lib.openblas_get_num_threads()


def set_nb_threads(n):
    openblas_lib.openblas_set_num_threads(n)


def get_nb_procs():
    return openblas_lib.openblas_get_num_procs()


class NbThreads(object):
    def __init__(self, nb_threads):
        self.old_nb_threads = get_nb_threads()
        self.nb_threads = nb_threads

    def __enter__(self):
        set_nb_threads(self.nb_threads)

    def __exit__(self, *args):
        set_nb_threads(self.old_nb_threads)


set_nb_threads(int(os.popen("cat /proc/cpuinfo | grep \"cpu cores\" | sed '1!d' | tail -c 2", "r").readline()))
