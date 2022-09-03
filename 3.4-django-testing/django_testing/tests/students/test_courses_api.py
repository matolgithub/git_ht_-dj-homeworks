import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


def test_example():
    assert True, "Just test example"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory
