import pytest
from django.contrib.auth.models import User


from pytest_factoryboy import register
from tests.factories import UserFactory, AuthorFactory, BookFactory


register(UserFactory)
register(AuthorFactory)
register(BookFactory)


# @pytest.fixture()
# def user(db):
#     print("create user")
#     user = User.objects.create_user("test_user")
#     return user


# @pytest.fixture()
# def new_user_factory(db):
#     def create_app_user(
#         username: str,
#         password: str,
#         first_name: str = "first_name",
#         last_name: str = "last_name",
#         email: str = "email",
#         is_superuser: bool = False,
#         is_staff: bool = False,
#         is_active: bool = True,
#     ):
#         return User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_superuser=is_superuser,
#             is_staff=is_staff,
#             is_active=is_active,
#         )

#     return create_app_user


# @pytest.fixture()
# def user_a(db, new_user_factory):
#     return new_user_factory("Ajay8989", "password")


# @pytest.fixture()
# def user_b(db, new_user_factory):
#     return new_user_factory("Ajay9000", "password")
