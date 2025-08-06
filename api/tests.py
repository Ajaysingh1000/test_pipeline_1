from django.test import TestCase

# Create your tests here.

import pytest


# @pytest.fixture(scope="module")
# def fixture_1():
#     # print("\n")
#     print("fixture_1")
#     print("fixture_1")
#     return 1


@pytest.fixture
def yield_fixture():
    print("start test phase")
    yield 6
    print("end test phase")


def test_example(yield_fixture):
    print("test")
    num = yield_fixture
    assert num == 6


# @pytest.mark.slow
# def test_example():
#     print("test")
#     assert 1 == 1


# def test_example1(fixture_1):
#     print("test1")
#     num = fixture_1
#     assert num == 1


# def test_example2(fixture_1):
#     print("test2")
#     num = fixture_1
#     assert num == 1
