from my_sum import my_sum
import pytest

def test_sum_int():
    # print('testing integers')
    assert my_sum([1,2,3]) == 6.0, 'should be 6.0'

def test_sum_float():
    # print('testing floats')
    assert my_sum([1,2,3.1]) == 6.1, 'should be 6.1'

def test_sum_numinstr():
    # print('testing floats')
    assert my_sum(['1','2','3.1']) == 6.1, 'should be 6.1'

def test_sum_not_numbers():
    with pytest.raises(Exception):
        assert my_sum(['one','two',3.1])
