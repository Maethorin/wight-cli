#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wight load testing
# https://github.com/heynemann/wight

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com
import mock
from nose.plugins.attrib import attr


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from preggy import expect

from wight.models import UserData
from wight.cli.default import SetDefaultController, GetDefaultController

from tests.unit.base import TestCase


class TestSetDefaultController(TestCase):

    def authenticate(self, ctrl):
        ctrl.app.user_data = UserData(target="Target")
        ctrl.app.user_data.token = "token-value"

    def test_set_team(self):
        ctrl = self.make_controller(SetDefaultController, conf=self.fixture_for('test.conf'), team='team-blah', project=None)
        self.authenticate(ctrl)
        ctrl.default()
        ud = UserData.load()
        expect(ud.team).to_equal("team-blah")
        expect(hasattr(ud, "project")).to_be_false()

    def test_set_project(self):
        ctrl = self.make_controller(SetDefaultController, conf=self.fixture_for('test.conf'), team=None, project='project-blah')
        self.authenticate(ctrl)
        ctrl.default()
        ud = UserData.load()
        expect(ud.project).to_equal("project-blah")
        expect(hasattr(ud, "team")).to_be_false()


class TestGetDefaultController(TestCase):

    def authenticate(self, ctrl):
        ctrl.app.user_data = UserData(target="Target")
        ctrl.app.user_data.token = "token-value"

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_default_team(self, mock_stdout):
        get_ctrl = self.make_controller(GetDefaultController, conf=self.fixture_for('test.conf'))
        self.authenticate(get_ctrl)
        get_ctrl.app.user_data.set_default(team="team-blah")
        get_ctrl.default()
        expect(mock_stdout.getvalue()).to_be_like("Default team is 'team-blah'. Default project not set.")

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_default_project(self, mock_stdout):
        get_ctrl = self.make_controller(GetDefaultController, conf=self.fixture_for('test.conf'))
        self.authenticate(get_ctrl)
        get_ctrl.app.user_data.set_default(project="project-blah")
        get_ctrl.default()
        expect(mock_stdout.getvalue()).to_be_like("Default team not set. Default project is 'project-blah'.")

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_default_team_and_project(self, mock_stdout):
        get_ctrl = self.make_controller(GetDefaultController, conf=self.fixture_for('test.conf'))
        self.authenticate(get_ctrl)
        get_ctrl.app.user_data.set_default(team="team-blah", project="project-blah")
        get_ctrl.default()
        expect(mock_stdout.getvalue()).to_be_like("Default team is 'team-blah'. Default project is 'project-blah'.")
