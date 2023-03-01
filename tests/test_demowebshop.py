import os

from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser

from utils.base_session import BaseSession

load_dotenv()


def test_login(demoshop_api):
    demoshop_api.open('')
    demoshop_api.element('.account').should(have.text(os.getenv('LOGIN')))


def test_open_books_page(demoshop_api):
    demoshop_api.open('/books')
    demoshop_api.element('.page-title').should(have.text('Books'))


def test_open_profile_page(demoshop_api):
    demoshop_api.open('')
    browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
    browser.element('#FirstName').should(have.value('test'))
    browser.element('#LastName').should(have.value('test'))
    browser.element('#Email').should(have.value(os.getenv('LOGIN')))
    browser.element('[checked="checked"]').should(have.value('M'))


def test_search(demoshop_api):
    demoshop_api.open('')
    browser.element('[id="small-searchterms"]').click()
    browser.element('[id="small-searchterms"]').should(be.blank).type('Copy of Computing and Internet EX')
    browser.element('[type="submit"]').click()
    browser.element('.product-grid').should(have.text('Copy of Computing and Internet EX'))


def test_open_orders_page(demoshop_api):
    demoshop_api.open('/customer/orders')
    demoshop_api.element('.page-title').should(have.text('My account - Orders'))


def test_change_password(demoshop_api):
    demoshop_api.open('/customer/changepassword')
    browser.element('#OldPassword').click()
    browser.element('#OldPassword').should(be.blank).type(os.getenv("PASSWORD"))
    browser.element('#NewPassword').click()
    browser.element('#NewPassword').should(be.blank).type(os.getenv("PASSWORD"))
    browser.element('#ConfirmNewPassword').click()
    browser.element('#ConfirmNewPassword').should(be.blank).type(os.getenv("PASSWORD"))
    browser.element('.change-password-button').click()
    demoshop_api.element('.result').should(have.text('Password was changed'))


def test_logout(demoshop_api):
    demoshop_api.open('')
    demoshop_api.element('.ico-logout').click()
    demoshop_api.element('.ico-login').should(have.text('Log in'))
    reg = BaseSession(os.getenv("API_URL"))
    response = reg.get('/logout', allow_redirects=False)
    assert response.status_code == 302
