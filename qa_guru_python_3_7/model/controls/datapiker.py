from selene.support.shared import browser


def datepicker_react_input(selector, *, year, month, day):
    browser.element(selector).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'[value="{month}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'[value="{year}"]').click()
    browser.element(f'.react-datepicker__day--0{day}').click()



#datetime_view_format = '%d %B,%Y'
#"12 December, 1990"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def datepicker_birthday_format(selector, *, year, month, day):
    birthday = (f'{day} {months[month]},{year}')
    return birthday


