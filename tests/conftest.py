import os
import pytest
from selene.support.shared import browser
import pytest
from utils.base_session import BaseSession
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope="session")
def examp_api():
    return BaseSession(os.getenv("REG_API"))


@pytest.fixture(scope="session")
def demoshop_api():
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    demoshop = BaseSession(os.getenv("API_URL"))
    resource = demoshop.post('/login', data={'Email': os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD')},
                                 allow_redirects=False)
    authorization_cookie = resource.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser

