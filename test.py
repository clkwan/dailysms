from dailysms import *


def test_convert_time():
    '''Unit test for convert time'''
    # test 1
    test1_time = convert_time('9:30')
    print(test1_time)
    # test 2
    test1_time = convert_time('11:30')
    print(test1_time)


def test_get_traffic():
    '''Unit test for gmaps traffic time'''
    print(get_traffic())


test_convert_time()
test_get_traffic()
