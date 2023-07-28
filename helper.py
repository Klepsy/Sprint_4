from faker import Faker
import random as r

class User():
    fake_ru = Faker('ru_Ru')
    fake_en = Faker('en_US')
    name = fake_ru.first_name()
    last_name = fake_ru.last_name()
    email = fake_en.email()
    address = r.choice(['Санкт-Петербург', 'Лениниградская область']) + ', ' + 'ул. ' + fake_ru.street_name()
    phone = r.randint(70000000000, 99999999999)
    delivery_date = str(r.randint(1, 30)) + '.' + str(r.randint(8, 12)) + '.' + '2023'
    comment = str(fake_ru.text())