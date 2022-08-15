from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

# Create your views here.
from blogposting.forms import AuthorForms, SendEmailForms
from blogposting.models import Course, Author


# view for list of courses for template courses_list.html
class Courses(ListView):
    model = Course

# for next homework
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('specialisation')
        return qs


# view for every course in courses list
class ReadCourse(DetailView):
    model = Course

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('specialisation').prefetch_related('authors')
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['authors_name'] = data['object'].\
            authors.\
            all().\
            select_related("user").\
            prefetch_related('study_organizations')
        return data


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
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("user").prefetch_related('study_organizations')
        return qs


class AuthorDetail(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['course_set'] = data['object'].\
            course_set.\
            all().\
            select_related("specialisation").\
            only("pk", "course_name", "specialisation__specialisation_name")
        return data


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForms


class SendEmail(FormView):
    form_class = SendEmailForms
    success_url = '/courses/'
