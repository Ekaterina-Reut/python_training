from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, group_data):
        self.modify_group_by_index(0, group_data)

    def modify_group_by_index(self, index, group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open edit page
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group_data)
        # submit group updating
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

