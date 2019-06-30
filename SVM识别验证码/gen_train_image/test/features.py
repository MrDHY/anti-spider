import pytest
from gen_train_image.last_img import together_path, ergodic


def test1():
    print ('test_1')
    assert together_path(1) == ['./0/1']


def test2():
    print ('test_2')
    assert ergodic('./test_file') == ['1']

if __name__ == '__main__':
    pytest.main("-s features.py")