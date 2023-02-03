from .page import Page


class WelcomePage(Page):

    to_login_button = ('id', 'com.ajaxsystems:id/login')
    to_signup_button = ('id', 'com.ajaxsystems:/')

    def press_to_login_btn(self):
        self.click(self.to_login_button)

