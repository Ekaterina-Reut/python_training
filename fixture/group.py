class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group_details(self, group):
        self.app.set_value_to_element(name="group_name", value=group.name)
        self.app.set_value_to_element(name="group_header", value=group.header)
        self.app.set_value_to_element(name="group_footer", value=group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_details(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # open edit page
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_details(group)
        # submit group updating
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()