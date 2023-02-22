from selene.support.shared import browser

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

class Birthday:
    def __init__(self, selector, year, month, day):
        self.selector = selector
        self.year = year
        self.month = month
        self.day = day

    def datepicker_react_input(self):
        browser.element(self.selector).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{self.month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{self.year}"]').click()
        browser.element(f'.react-datepicker__day--0{self.day}').click()


    def datepicker_birthday_format(self):
        birthday = f'{self.day} {months[self.month]},{self.year}'
        return birthday

#datetime_view_format = '%d %B,%Y'
#"12 December, 1990"
