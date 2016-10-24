# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest

from dictator import Dictator


@pytest.fixture
def dictator_inst():
    return Dictator(decode_responses=True)


@pytest.fixture(params=[
    'some-test-value',
    ['1', '2', '3'],
    {'a': 'A', 'b': 'B'},
])
def key_value(request):
    key = 'some-test-key'
    value = request.param
    dc = dictator_inst()
    dc[key] = value

    yield key, value
    del dc[key]
