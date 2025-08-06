import factory

from django.contrib.auth.models import User
from api.models import Author, Book
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    password = fake.password()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = fake.name()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = fake.name()
    description = fake.text()
    author = factory.SubFactory(AuthorFactory)
    # author_id = AuthorFactory().Meta.model.pk
