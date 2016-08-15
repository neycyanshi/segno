# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 -- Lars Heuer - Semagia <http://www.semagia.com/>.
# All rights reserved.
#
# License: BSD License
#
"""\
Tests against the ``utils`` module.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - http://www.semagia.com/
:license:      BSD License
"""
from __future__ import absolute_import, unicode_literals
from nose.tools import ok_, eq_, raises
from segno import utils, consts


def test_get_border():
    border = utils.get_border(1, None)
    eq_(4, border)
    border = utils.get_border(1, 3)
    eq_(3, border)


def test_get_border2():
    border = utils.get_border(consts.VERSION_M1, 1)
    eq_(1, border)
    border = utils.get_border(consts.VERSION_M1, None)
    eq_(2, border)


def test_get_border3():
    border = utils.get_border(3, 0)
    eq_(0, border)
    border = utils.get_border(3, None)
    eq_(4, border)


def test_get_symbol_size():
    version = 1
    matrix_size = 21
    border = 0
    width, height = utils.get_symbol_size(version, border=border)
    eq_((matrix_size, matrix_size), (width, height))
    border = 4
    width, height = utils.get_symbol_size(1)
    eq_((matrix_size + 2 * border, matrix_size + 2 * border), (width, height))


def test_get_symbol_size_micro():
    version = consts.VERSION_M2
    matrix_size = 13
    border = 0
    width, height = utils.get_symbol_size(version, border=border)
    eq_((matrix_size, matrix_size), (width, height))
    border = 2
    width, height = utils.get_symbol_size(version)
    eq_((matrix_size + 2 * border, matrix_size + 2 * border), (width, height))


if __name__ == '__main__':
    import nose
    nose.core.runmodule()