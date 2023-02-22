from selene import have
from selene.support.shared import browser


class Gender:
    def __init__(self, selector, value):
        self.selector = selector
        self.value = value

    def gender(self):
        browser.all(self.selector).element_by(have.value(self.value)).element('..').click()
