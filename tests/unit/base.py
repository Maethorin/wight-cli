#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wight load testing
# https://github.com/heynemann/wight

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from os.path import dirname, abspath, join
from unittest import TestCase as PythonTestCase
import socket

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from mock import Mock
from cement.utils import test

ROOT_PATH = abspath(join(dirname(__file__), '..'))


def focus(*args, **kwargs):
    def wrap_ob(ob):
        setattr(ob, 'focus', 1)
        return ob
    return wrap_ob


class TestCase(test.CementTestCase):
    def clean_calls(self):
        self.calls_made = []

    def record_calls(self, *args, **kw):
        self.calls_made.append((args, kw))

    def make_controller(self, cls, app=None, *args, **kw):
        if app is None:
            app = self.make_app(argv=args)
            app.setup()

        pargs = Mock(**kw)
        controller = cls(pargs=pargs)
        controller.app = app
        controller.log = Mock()

        return controller

    def fixture_for(self, filename):
        return join(ROOT_PATH, 'tests', 'fixtures', filename)
