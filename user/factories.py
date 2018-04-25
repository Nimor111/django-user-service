import factory
from faker import Factory

from user.models import User


faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyAttribute(lambda _: faker.name())
    last_name = factory.LazyAttribute(lambda _: faker.name())
    password = factory.LazyAttribute(lambda _: faker.password())
    email = factory.LazyAttribute(lambda _: faker.email())
