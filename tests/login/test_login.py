import pytest
import time
from loguru import logger

logger.add("./loggs/file_{time}.log")

LOGIN = 'qa.ajax.app.automation@gmail.com'
PASSWORD = 'qa_automation_password'


def test_login_positive(user_login_fixture, welcome_fixture, main_page_fixture):
    logger.debug('Logging from test_login_positive')
    welcome_fixture.press_to_login_btn()
    time.sleep(5)
    user_login_fixture.input_login(LOGIN)
    user_login_fixture.input_password(PASSWORD)
    user_login_fixture.press_submit_button()
    time.sleep(5)

    assert (main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/hubAdd'))) is True
    main_page_fixture.logout()
    logger.debug('End logging')


def test_user_login_no_credentials(user_login_fixture, welcome_fixture, main_page_fixture):
    logger.debug('Logging from test_user_login_no_credentials')
    welcome_fixture.press_to_login_btn()
    time.sleep(5)
    user_login_fixture.press_submit_button()
    time.sleep(5)

    assert (main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/hubAdd'))) is False
    logger.debug('End logging')


def test_user_login_incorrect_login(user_login_fixture, welcome_fixture, main_page_fixture):
    welcome_fixture.press_to_login_btn()
    time.sleep(5)
    user_login_fixture.input_login('incorrect@email.com')
    user_login_fixture.input_password('qa_automation_password')
    user_login_fixture.press_submit_button()
    time.sleep(5)

    # assert main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/snackbar_action')) is True
    assert main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/hubAdd')) is False


def test_user_login_incorrect_password(user_login_fixture, welcome_fixture, main_page_fixture):
    welcome_fixture.press_to_login_btn()
    time.sleep(5)
    user_login_fixture.input_login('qa.ajax.app.automation@gmail.com')
    user_login_fixture.input_password('incorrect_pass')
    user_login_fixture.press_submit_button()
    time.sleep(5)

    # assert main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/snackbar_action')) is True
    assert main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/hubAdd')) is False


@pytest.mark.parametrize('login, password, expected_result', [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
    ('incorrect@email.com', 'incorrect_pass', False),
    ('qa.ajax.app.automation@gmail.com', 'incorrect_pass', False),
    ('incorrect@email.com', 'qa_automation_password', False),
    ('', '', False),
    ('qa.ajax.app.automation@gmail.com', '', False),
    ('', 'qa_automation_password', False)
])
def test_user_login_param(login, password, expected_result, user_login_fixture, welcome_fixture, main_page_fixture, caplog):
    logger.debug('Logging from test_user')
    welcome_fixture.press_to_login_btn()
    time.sleep(5)
    user_login_fixture.input_login(login)
    logger.info(f"Login is: {login}")
    user_login_fixture.input_password(password)
    logger.info(f"Password is: {password}")

    user_login_fixture.press_submit_button()
    time.sleep(5)

    assert (main_page_fixture.is_visible(('id', 'com.ajaxsystems:id/hubAdd'))) == expected_result

    main_page_fixture.logout()
    logger.debug('End logging')
