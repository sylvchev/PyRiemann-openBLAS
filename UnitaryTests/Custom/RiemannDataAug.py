


def test_Riemann_data_aug():

def _get_state(old, new, func_name):
    if abs( old.sum() - new.sum() ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False