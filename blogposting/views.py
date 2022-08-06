from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from blogposting.forms import AuthorForms
from blogposting.models import Course, Author


# view for list of courses for template courses_list.html
class Courses(ListView):
    model = Course

# for next homework
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.select_related('specialisation')
#         return qs


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


# add view for deleted course
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("blogposting:courses_list")


# author part

class AuthorsList(ListView):
    model = Author

# # for next homework
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.select_related("user").prefetch_related('study_organizations')
#         return qs

class AuthorDetail(DetailView):
    model = Author


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForms
