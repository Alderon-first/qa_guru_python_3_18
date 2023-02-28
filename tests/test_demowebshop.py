import os
from selene import have, be
from selene.support.shared import browser
from utils.base_session import BaseSession
from dotenv import load_dotenv
load_dotenv()


def test_login(demoshop_api):
    demoshop_api.open('')
    demoshop_api.element('.account').should(have.text(os.getenv('LOGIN')))


def test_open_page_books(demoshop_api):
    demoshop_api.open('/books')
    demoshop_api.element('.page-title').should(have.text('Books'))


def test_open_page_profile(demoshop_api):
    demoshop_api.open('')
    browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
    browser.element('#FirstName').should(have.value('test'))
    browser.element('#LastName').should(have.value('test'))
    browser.element('#Email').should(have.value(os.getenv('LOGIN')))
    browser.element('[checked="checked"]').should(have.value('M'))

def test_sesrch(demoshop_api):
    demoshop_api.open('')
    browser.element('[id="small-searchterms"]').click()
    browser.element('[id="small-searchterms"]').should(be.blank).type('Copy of Computing and Internet EX')
    browser.element('[type="submit"]').click()
    browser.element('.product-grid').should(have.text('Copy of Computing and Internet EX'))



def test_logout(demoshop_api):
    demoshop_api.open('')
    demoshop_api.element('.ico-logout').click()
    demoshop_api.element('.ico-login').should(have.text('Log in'))
    reg = BaseSession(os.getenv("API_URL"))
    response = reg.get('/logout', allow_redirects=False)
    assert response.status_code == 302





