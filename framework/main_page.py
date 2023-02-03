from .page import Page
import time


class MainPage(Page):

    hamburger_menu = ('id', 'com.ajaxsystems:id/menuDrawer')
    hamburger_menu_x = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                               'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                               'androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/'
                               'android.widget.LinearLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/'
                               'android.widget.ImageView')
    add_hub_button = ('id', 'com.ajaxsystems:id/hubAdd')
    settings_button = ('id', 'com.ajaxsystems:id/settings')
    logout_button = ('id', 'com.ajaxsystems:id/accountInfoLogoutNavigate')

    def press_menu_btn(self):
        self.click(self.hamburger_menu)

    def press_add_hub_btn(self):
        self.click(self.add_hub_button)

    def logout(self):
        if self.is_visible(self.add_hub_button):
            self.click(self.hamburger_menu)
            time.sleep(3)
            self.click(self.settings_button)
            time.sleep(3)
            self.click(self.logout_button)

