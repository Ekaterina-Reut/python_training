class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.app.set_value_to_element(name="group_name", value=group.name)
        self.app.set_value_to_element(name="group_header", value=group.header)
        self.app.set_value_to_element(name="group_footer", value=group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select_first_group
        wd.find_element_by_name("selected[]").click()
        # submit_deletion
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()