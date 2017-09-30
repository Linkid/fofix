#!/usr/bin/python
# -*- coding: utf-8 -*-

# FoFiX
# Copyright (C) 2017 FoFiX team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import tempfile
import unittest

from fofix.core import Config
from fofix.core.Config import Config as ConfigClass
from fofix.core.Config import MyConfigParser


class ConfigTest(unittest.TestCase):
    def test_set(self):
        pass

    def test_load(self):
        fp = tempfile.TemporaryFile()

    def test_get(self):
        pass


class MyConfigParserTest(unittest.TestCase):
    def test_write(self):
        pass
    def test_read(self):
        pass
    def test_writeController(self):
        pass
    def test_writePlayer(self):
        pass
    def test_get(self):
        pass
    def test_set(self):
        pass


class ConfigTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_get(self):
        pass
    def test_getOptions(self):
        pass
    def test_getTipText(self):
        pass
    def test_getDefault(self):
        pass
    def test_set(self):
        pass
