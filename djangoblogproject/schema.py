import graphene
from graphene_django import DjangoObjectType

from blogposting.models import Course, Author, Student, Specialisation

from django.contrib.auth.models import User


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'authors', 'specialisation')


class SpecialisationType(DjangoObjectType):
    class Meta:
        model = Specialisation
        fields = ('specialisation_name', 'study_time')


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('status', 'user')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username')


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ('user', 'course')


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    course_type = graphene.List(CourseType)
    author_type = graphene.Field(AuthorType)
    user_type = graphene.List(UserType)
    student_type = graphene.List(StudentType)
    specialisation_type = graphene.Field(SpecialisationType)

    def resolve_course_type(self, info):
        return Course.objects.all()

    def resolve_author_type(self, info):
        return Author.objects.all()

    def resolve_user_type(self, info):
        return User.objects.all()

    def resolve_student_type(self, info):
        return Student.objects.all()

    def resolve_specialisation_type(self, info):
        return Specialisation.objects.all()

schema = graphene.Schema(query=Query)
