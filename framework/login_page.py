from .page import Page


class LoginPage(Page):

    login_input = ('id', 'com.ajaxsystems:id/login')
    password_input = ('id', 'com.ajaxsystems:id/password')
    submit_button = ('id', 'com.ajaxsystems:id/next')
    pop_up_error_message_text = ('id', 'com.ajaxsystems:id/snackbar_text')
    report_a_problem_button = ('id', 'com.ajaxsystems:id/snackbar_action')

    def input_login(self, login):
        self.send_keys(self.login_input, login)

    def input_password(self, password):
        self.send_keys(self.password_input, password)

    def press_submit_button(self):
        self.click(self.submit_button)

    def press_report_button(self):
        self.click(self.report_a_problem_button)

