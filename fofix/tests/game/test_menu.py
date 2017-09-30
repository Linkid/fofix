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

from fretwork import log

#from fofix.game.Menu import Choice
from fofix.core import Config
from fofix.core import Version
from fofix.core.GameEngine import GameEngine
from fofix.game.Menu import Menu


def my_callback():
    print("I'm a callback")


class MenuTest(unittest.TestCase):

    def setUp(self):
        # set log file
        fp = tempfile.TemporaryFile()
        log.setLogfile(fp)

        # set config file
        config_file = Version.PROGRAM_UNIXSTYLE_NAME + ".ini"
        self.config = Config.load(config_file, setAsDefault=True)

        # set choices
        choices = [
            ("Choice 1", my_callback),
        ]

        # init the engine
        engine = GameEngine(self.config)

        # init the menu
        self.menu = Menu(engine, choices)

    def test_init(self):
        self.assertGreater(len(self.menu.choices), 0)
        self.assertEqual(self.menu.currentIndex, 0)

    #def test_scrollDown(self):
    #    current_index = self.menu.currentIndex
    #    nb_choices = len(self.choices)

    #    # first scroll
    #    self.menu.scrollDown()
    #    self.assertEqual(current_index + 1, 0)
    #    # second scroll: go back
    #    self.menu.scrollDown()
    #    self.assertEqual(current_index, 0)

    #def test_scrollUp(self):
    #    pass


#class ChoiceTest(unittest.TestCase):
#    def test_init_choice(self):
#        text = "My text >"
#        callback = ""  # TODO
#        choice = Choice(text, callback)
#
#        self.assertEqual(choice.text, text[:-2])
#        self.assertTrue(choice.isSubMenu)
#        self.assertEqual(choice.valueIndex, 0)
#
#    def test_init_choice_other(self):
#        text = "My text"
#        callback = [0, 1]
#        choice = Choice(text, callback)
#
#    def test_selectNextValue_with_two_values(self):
#        text = "My text"
#        callback = ""  # TODO
#        values = [0, 1]
#        choice = Choice(text, callback, values=values)
#
#        # first value
#        value_index = choice.valueIndex
#        # second value
#        choice.selectNextValue()
#        self.assertEqual(choice.valueIndex, value_index + 1)
#        # first value
#        choice.selectNextValue()
#        self.assertEqual(choice.valueIndex, value_index)
#
#    def test_selectPreviousValue_with_two_values(self):
#        text = "My text"
#        callback = ""  # TODO
#        values = [0, 1]
#        value_index = 1  # second value
#        choice = Choice(text, callback, values=values, valueIndex=value_index)
#
#        # first value
#        choice.selectPreviousValue()
#        self.assertEqual(choice.valueIndex, value_index - 1)
#        # second value
#        choice.selectPreviousValue()
#        self.assertEqual(choice.valueIndex, value_index)
#
#    def test_getText_menu(self):
#        text = "My text"
#        callback = ""  # TODO
#        choice = Choice(text, callback)
#
#        choice.getText()
#
#    def test_getText_submenu(self):
#        pass