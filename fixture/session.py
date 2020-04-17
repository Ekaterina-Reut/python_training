class SessionHelper:

    def __init__(self, app):
        self.app = app

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.change_field_value(name="user", value=username)
        self.app.change_field_value(name="pass", value=password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
