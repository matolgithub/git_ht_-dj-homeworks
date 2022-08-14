from django.shortcuts import render
from django.views.generic import ListView

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().order_by('group')
    context = {'students': students}

    return render(request, template_name=template, context=context)


# class StudentListView(ListView):
#     template = 'school/students_list.html'
#     model = Student
#     ordering = 'group'
#     queryset = Student.objects.all().prefetch_related('teacher')





