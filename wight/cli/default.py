#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wight load testing
# https://github.com/heynemann/wight

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from cement.core import controller

from wight.cli.base import WightBaseController


class GetDefaultController(WightBaseController):
    class Meta:
        label = 'get-default'
        stack_on = 'base'
        description = 'Shows the defined default team and/or project.'
        config_defaults = dict()

        arguments = [
            (['--conf'], dict(help='Configuration file path.', default=None, required=False)),
        ]

    @controller.expose(hide=False, aliases=["get-default"], help='Shows the defined default team and/or project.')
    @WightBaseController.authenticated
    def default(self):
        self.load_conf()
        user_data = self.app.user_data
        self.line_break()
        self.write("Default team is '%s'." % user_data.team)
        self.line_break()


class SetDefaultController(WightBaseController):
    class Meta:
        label = 'set-default'
        stack_on = 'base'
        description = 'Define default team and/or project to be used in subsequent commands.'
        config_defaults = dict()

        arguments = [
            (['--conf'], dict(help='Configuration file path.', default=None, required=False)),
            (['team'], dict(help='The name of the team to be used as default')),
            (['project'], dict(help='The name of the project to be used as default')),
        ]

    @controller.expose(hide=False, aliases=["set-default"], help='Define default team and/or project to be used in subsequent commands.')
    @WightBaseController.authenticated
    def default(self):
        self.load_conf()
        team = self.arguments.team
        project = self.arguments.project
        self.app.user_data.set_default(team=team, project=project)
        self.app.user_data.save()
