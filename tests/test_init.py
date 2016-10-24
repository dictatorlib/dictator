# -*- coding: utf-8 -*-

from __future__ import absolute_import


def test_init_normal(dictator_inst):
    assert dictator_inst.host == 'localhost'
    assert dictator_inst.port == 6379
    assert dictator_inst.db == 0
