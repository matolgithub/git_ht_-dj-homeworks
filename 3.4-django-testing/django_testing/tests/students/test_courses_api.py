import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


# def test_example():
#     assert True, "Just test example"


# ---------Fixtures and factories block

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def localhost_url():
    URL = 'http://127.0.0.1:8000/api/v1/courses'
    return URL


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


# -----------Tests block

# Test_1
@pytest.mark.django_db
def test_course_1(client, course_factory, localhost_url, course_quant=5):
    # Arrange
    course = course_factory(_quantity=course_quant)
    for item in range(course_quant):
        url = localhost_url + "/" + str(course[item].id) + "/"
        # Act
        response = client.get(url)
        # Assert
        assert response.status_code == 200
        assert response.data['name'] == course[item].name


# Test_2
@pytest.mark.django_db
def test_2():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_3
@pytest.mark.django_db
def test_3():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_4
@pytest.mark.django_db
def test_4():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_5
@pytest.mark.django_db
def test_5():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_6
@pytest.mark.django_db
def test_6():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_7
@pytest.mark.django_db
def test_7():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass


# Test_8
@pytest.mark.django_db
def test_8():
    # Arrange
    pass
    # Act
    pass
    # Assert
    pass
