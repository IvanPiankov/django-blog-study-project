from django.shortcuts import render

# Create your views here.
from blogposting.models import Author, Course


def index(request):
    author = Author.objects.all()
    context = {
        "author": author
    }
    return render(request, 'blogposting/index.html', context=context)


def courses_list(request):
    courses_list = Course.objects.all()
    context = {
        "courses": courses_list
    }
    return render(request, 'blogposting/courses_list.html', context=context)

def course(request):
    course = Course.objects.filter()
    context = {

    }
    return render(request, 'blogposting/course.html', context=context)