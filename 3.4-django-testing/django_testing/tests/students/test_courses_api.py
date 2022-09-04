import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course
from students.serializers import CourseSerializer


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
def test_coursefilterid_3(client, course_factory, host_url, quantity=10):
    # Arrange
    courses = course_factory(_quantity=quantity)
    # Act
    response = client.get(host_url, {'id': courses[0].id})
    # Assert
    assert response.status_code == 200 and response.status_text == "OK"
    assert len(response.data) == 1
    assert response.data[0]['id'] == courses[0].id


# Test_4
@pytest.mark.django_db
def test_coursefiltername_4(client, course_factory, host_url, quantity=10):
    # Arrange
    courses = course_factory(_quantity=quantity)
    # Act
    response = client.get(host_url, {'name': courses[0].name})
    # Assert
    assert response.status_code == 200 and response.status_text == "OK"
    assert len(response.data) == 1
    assert response.data[0]['name'] == courses[0].name


# Test_5
@pytest.mark.django_db
def test_course_create_5(client, course_factory, host_url, new_course='Django'):
    # Arrange
    # Act
    response = client.post(path=host_url, data={'name': new_course})
    # Assert
    assert response.status_code == 201 and response.status_text == 'Created'
    assert response.data['name'] == new_course


# Test_6
@pytest.mark.django_db
def test_course_update_6(client, course_factory, host_url, update_course='Django'):
    # Arrange
    course = course_factory(_quantity=1)
    # Act
    response = client.patch(path=f"{host_url}+{course[0].id}/", data={'name': update_course})
    # Assert
    assert response.status_code == 200 and response.status_text == 'OK'
    assert response.data['name'] == update_course


# Test_7
@pytest.mark.django_db
def test_deletecourse_7(client, course_factory, host_url, quantity=3):
    # Arrange
    course = course_factory(_quantity=quantity)
    for item in range(quantity):
        # Act
        response = client.delete(path=f"{host_url}+{course[item].id}/")
        # Assert
        assert response.status_code == 204
        assert response.status_text == "No Content"


# Test_8
@pytest.mark.parametrize(
    ['num_students', 'valid_status'],
    (
        (0, 201),
        (1, 201),
        (20, 201),
        (21, 400),
        (50, 400)
    )
)
@pytest.mark.django_db
def test_max_students_8(num_students, valid_status):
    # Arrange
    for item in range(num_students):
        # Act
        response = CourseSerializer.valid_status_students(self=None, students=num_students)
        # Assert
        assert response == valid_status
