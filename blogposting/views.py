from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView

# Create your views here.
from blogposting.models import Author, Course


# view for list of courses for template courses_list.html
class Courses(ListView):
    model = Course


# view for every course in courses list
class ReadCourse(DetailView):
    model = Course

#
# class CourseCreateView(CreateView):
#     model = ReadCourse
#     fields = ['course_name', 'authors', 'specialisation', 'study_organizations']