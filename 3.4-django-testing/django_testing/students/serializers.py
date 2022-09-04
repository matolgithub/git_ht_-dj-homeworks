from rest_framework import serializers

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def valid_status_students(self, students):
        valid_status = [{'positive': 201}, {'negative': 400}]
        if students > MAX_STUDENTS_PER_COURSE:
            return valid_status[1]['negative']
        return valid_status[0]['positive']
