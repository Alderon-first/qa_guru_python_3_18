import pytest
from qa_guru_python_3_14.utils import attach
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
import selenium


@pytest.fixture(scope="function", autouse=True)
def browser_managment():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = selenium.webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    browser.config.base_url = 'https://event-dev.pikemedia.live/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()


