from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from blogposting.models import Author, Course


# view for list of courses for template courses_list.html
class Courses(ListView):
    model = Course


# view for every course in courses list
class ReadCourse(DetailView):
    model = Course


# add class view for create course object
class CourseCreateView(CreateView):
    model = Course
    fields = ['course_name', 'authors', 'specialisation', 'study_organizations']


# add class view for updated course object
class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_name', 'authors', 'specialisation', 'study_organizations']
