from selene.support.shared import browser


class Drop:
    def __init__(self, id_option, text):
        self.id_option = id_option
        self.text = text

    def select(self):
        browser.element(f'#react-select-{self.id_option}-input').type(self.text).press_enter()
