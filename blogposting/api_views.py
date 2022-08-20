# ViewSets define the view behavior.
from rest_framework import viewsets

from blogposting.models import Course
from blogposting.serilalizers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

