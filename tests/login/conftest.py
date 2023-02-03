import pytest

from framework.login_page import LoginPage
from framework.welcome_page import WelcomePage
from framework.main_page import MainPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope='function')
def main_page_fixture(driver):
    yield MainPage(driver)


@pytest.fixture(scope='function')
def welcome_fixture(driver):
    yield WelcomePage(driver)