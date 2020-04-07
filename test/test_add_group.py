# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="gfgdf", header="gfgdf", footer="gfddfg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
