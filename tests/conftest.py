import subprocess
import time

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    android_caps = android_get_desired_capabilities()
    android_caps['udid'] = get_udid()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_caps)
    yield driver
    driver.quit()


def get_udid():

    call = subprocess.Popen(
        ['adb', 'devices'],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    cmd_result = call.communicate()
    result_lines = cmd_result[0].splitlines()
    if result_lines[1].decode('utf-8') == '':
        raise Exception('There is now devices connected')
    else:
        udid = result_lines[1].decode('utf-8').split()[0]
        return udid
