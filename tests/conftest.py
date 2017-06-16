# coding: utf-8


import pytest

from dictator import Dictator


@pytest.fixture
def dictator_inst():
    return Dictator(decode_responses=True)


@pytest.yield_fixture(params=[
    'some-test-value',
    ['1', '2', '3'],
    {'a': 'A', 'b': 'B'},
    set(['a', 'b', 'c', 'b']),
])
def key_value(request):
    key = 'some-test-key'
    value = request.param
    dc = dictator_inst()
    dc[key] = value

    yield key, value
    del dc[key]
