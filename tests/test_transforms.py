from cellpose.transforms import *

def test_random_rotate_and_resize__default():
    nimg = 2
    X = [np.random.rand(64, 64) for i in range(nimg)]

    random_rotate_and_resize(X)

def test_random_rotate_and_resize__use_skel():
    nimg = 2
    X = [np.random.rand(64, 64) for i in range(nimg)]

    random_rotate_and_resize(X, skel=True)