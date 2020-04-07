class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        self.app.change_field_value(name="group_name", value=group.name)
        self.app.change_field_value(name="group_header", value=group.header)
        self.app.change_field_value(name="group_footer", value=group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open edit page
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group updating
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
