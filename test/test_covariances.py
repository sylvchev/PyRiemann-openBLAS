import numpy as np
from pyriemann.covariances import Covariances
from nose.tools import assert_equal

n_trials, n_channels, n_samples = 2, 3, 100
X = np.random.randn(n_trials, n_channels, n_samples)

def test_covariances():
    cov = Covariances().fit(X)
    cm = cov.fit_transform(X)
    assert_equal(cov.get_params(), dict(estimator='scm'))
    assert_equal(cm.length, n_trials)
    assert_equal(cm.dim, n_channels)
    assert_equal(cm.shape, (n_trials, n_channels, n_channels))
    
