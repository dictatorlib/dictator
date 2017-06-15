# coding: utf-8


def test_get_item_normal(dictator_inst, key_value):
    key, value = key_value
    assert dictator_inst[key] == value


def test_get_item_method(dictator_inst, key_value):
    key, value = key_value
    assert dictator_inst.get(key) == value


def test_get_item_empty(dictator_inst):
    test_default = 'test-default'
    assert dictator_inst.get(
        'does-not-exist', test_default
    ) == test_default
