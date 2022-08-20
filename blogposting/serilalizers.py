
# Serializers define the API representation.
from rest_framework import serializers

from blogposting.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
