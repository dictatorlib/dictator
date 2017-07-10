# coding: utf-8
import pytest


def test_getitem_nonexist(dictator_inst, key_value):
    non_exist_key = 'non_exist'
    with pytest.raises(KeyError) as exc_info:
        _ = dictator_inst[non_exist_key]
    assert non_exist_key in str(exc_info)


def test_getitem_normal(dictator_inst, key_value):
    key, value = key_value
    assert dictator_inst[key] == value


def test_get_nonexist(dictator_inst, key_value):
    non_exist_key = 'non_exist'
    assert dictator_inst.get(non_exist_key) == None


def test_get_method(dictator_inst, key_value):
    key, value = key_value
    assert dictator_inst.get(key) == value


def test_get_empty(dictator_inst):
    test_default = 'test-default'
    assert dictator_inst.get(
        'does-not-exist', test_default
    ) == test_default
