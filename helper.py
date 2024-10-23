import random
import faker
from datetime import datetime, timedelta

fake = faker.Faker('ru_RU')


def generate_name():
    return fake.first_name()


def generate_surname():
    return fake.last_name()


def generate_phone(country_code='7', digits=10):
    return country_code + ''.join([str(random.randint(0, 9)) for _ in range(digits)])


def generate_address():
    street = fake.street_name()
    house_number = fake.building_number()
    return f"{street}, {house_number}"


def generate_date(days_in_future=30, date_format="%d.%m.%Y"):
    future_date = datetime.today() + timedelta(days=random.randint(1, days_in_future))
    return future_date.strftime(date_format)


def generate_comment(nb_words=5):
    return fake.sentence(nb_words=nb_words)
