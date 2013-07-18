#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wight load testing
# https://github.com/heynemann/wight

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

from wight.models import UserData
from tests.acceptance.base import LocalAcceptanceTest


class TestDefault(LocalAcceptanceTest):

    def test_can_set_team(self):
        team = "team-blah"
        result = self.execute("set-default", team=team)
        expected = "Default team set to 'team-blah'. Default project not set."
        expect(result).to_be_like(expected)
        ud = UserData.load()
        expect(ud.team).to_be_like(team)
