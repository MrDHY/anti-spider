import pytest
from captcha_recoginize.reconginize import reconginize


def test1():
    print('test_1')
    a = reconginize()
    text = a.recongnize_main('../images/0.jpeg')
    assert text == 'fm83'

if __name__ == '__main__':
    pytest.main("-s features.py")