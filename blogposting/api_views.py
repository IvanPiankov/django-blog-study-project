# ViewSets define the view behavior.
from rest_framework import viewsets

from blogposting.models import Course, Author
from blogposting.serilalizers import CourseSerializer, AuthorSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
