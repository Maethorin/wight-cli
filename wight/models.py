#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps, loads
from os import environ
from os.path import exists, expanduser


class UserData(object):
    DEFAULT_PATH = expanduser(environ.get('WIGHT_USERDATA_PATH', None) or "~/.wight")

    def __init__(self, target, token=None):
        self.target = target
        self.token = token

    def to_dict(self):
        user_data = {
            "target": self.target,
            "token": self.token,
        }

        if hasattr(self, "team"):
            user_data["team"] = self.team

        if hasattr(self, "project"):
            user_data["project"] = self.project

        return user_data

    def set_default(self, team=None, project=None):
        if team:
            self.team = team
        if project:
            self.project = project

    def save(self, path=None):
        if path is None:
            path = UserData.DEFAULT_PATH

        with open(path, 'w') as serializable:
            serializable.write(dumps(self.to_dict()))

    @classmethod
    def from_dict(cls, data):
        item = cls(
            target=data['target'],
            token=data.get('token', None),
        )
        if "team" in data:
            item.set_default(team=data["team"])
        if "project" in data:
            item.set_default(project=data["project"])
        return item

    @classmethod
    def load(cls, path=None):
        if path is None:
            path = UserData.DEFAULT_PATH

        if not exists(path):
            return None

        with open(path, 'r') as serializable:
            return cls.from_dict(loads(serializable.read()))
