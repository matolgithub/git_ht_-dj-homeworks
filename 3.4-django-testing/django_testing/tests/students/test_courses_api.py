import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


# ---------Fixtures and factories block

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def host_url():
    URL = '/api/v1/courses/'
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

# Example test
def test_example():
    assert True, "Just test example"


# Test_1
@pytest.mark.django_db
def test_course_1(client, course_factory, host_url, course_quant=1):
    # Arrange
    course = course_factory(_quantity=course_quant)
    for item in range(course_quant):
        url = host_url + str(course[item].id) + "/"
        # Act
        response = client.get(url)
        # Assert
        assert response.status_code == 200
        assert response.status_text == 'OK'
        assert response.data['name'] == course[item].name


# Test_2
@pytest.mark.django_db
def test_course_2(client, course_factory, host_url, quantity=5):
    # Arrange
    _ = course_factory(_quantity=quantity)
    # Act
    response = client.get(host_url)
    # Assert
    assert response.status_code == 200 and response.status_text == 'OK'
    assert len(response.data) == 5


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
