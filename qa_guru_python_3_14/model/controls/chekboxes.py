from selene import have
from selene.support.shared import browser



class Hobby:
    def __init__(self, selector, value):
        self.selector = selector
        self.value = value

    def hobby(self):
        browser.all(self.selector).element_by(have.text(self.value)).click()
