from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    year: str
    month: int
    day: int
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str
    message: str


user = User(first_name="Имя",
            last_name='Отчество',
            email='test@test.ru',
            gender='Female',
            phone='1234567890',
            year='1990',
            month=11,
            day=12,
            subject='Arts',
            hobby='Sports',
            file='resource/текст_1920-1080.jpg',
            address='currentAddress',
            state='NCR',
            city='Delhi',
            message='Сообщение')
