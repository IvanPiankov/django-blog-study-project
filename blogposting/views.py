from django.shortcuts import render
from django.views.generic import ListView

from django.views.generic.edit import CreateView

# Create your views here.
from blogposting.models import Author, Course

# view for list of courses for template courses_list.html
class Courses(ListView):
    model = Course




class CourseCreateView(CreateView):
    model = Course
    fields = ['course_name', 'authors', 'specialisation', 'study_organizations']