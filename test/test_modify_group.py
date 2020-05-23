# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_modify_some_group(app, db, check_ui):
    with allure.step('Add contact if group list is empty'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name='For modify'))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list and get new group data'):
        group_old = random.choice(old_groups)
    with allure.step('Set new group data'):
        group_new = Group(id=group_old.id, name="lhjg", header="ytrff", footer="qwew")
    with allure.step('When I modify the group %s from the list' % group_new):
     app.group.modify_group_by_id(group_old.id, group_new)
    with allure.step('Then the new group list is equal to the old list without the modified group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups.remove(group_old)
        old_groups.append(group_new)
        assert sorted(old_groups, key=Group.id_or_max) == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



# def test_modify_some_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='For modify'))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="lhjg", header="ytrff", footer="qwew")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='For modify'))
#     old_groups = app.group.get_group_list()
#     group = Group(name="New group")
#     group.id = old_groups[0].id
#     app.group.modify_first_group(group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='For modify'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='For modify'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)