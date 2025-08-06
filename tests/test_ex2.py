import pytest

from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_set_check_password(user):
#     user.set_password("test_password")
#     assert user.check_password("test_password") is True


# def test_set_check_password1(user):
#     user.username = "money_user"
#     print("money user")
#     assert user.username == "money_user"


# def test_user1(user_a):
#     print(user_a.username)
#     print(user_a.password)
#     assert user_a.username == "Ajay8989"


# def test_user2(user_b):
#     print(user_b.username)
#     print(user_b.password)
#     assert user_b.username == "Ajay9000"


# @pytest.mark.django_db
def test_user1(user_factory):
    user = user_factory.build()
    print(user.__dict__)
    assert True


def test_user2(user_factory):
    user = user_factory.build()
    print(user.__dict__)
    assert True


def test_author(author_factory):
    author = author_factory.build()
    print(author.__dict__)
    assert True


def test_book(author_factory, book_factory):
    book = book_factory.build()
    book.author = author_factory.build()
    print(book.__dict__)
    assert True
