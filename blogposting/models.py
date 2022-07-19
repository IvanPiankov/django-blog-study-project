from django.contrib.auth import get_user_model
from django.db import models


class StudyOrganization(models.Model):
    ORGANIZATION_UN = "U"
    ORGANIZATION_SH = "S"
    ORGANIZATION_COLL = "C"

    STATUS_CHOICES = [
        (ORGANIZATION_UN, "University"),
        (ORGANIZATION_SH, "School"),
        (ORGANIZATION_COLL, "College"),
    ]
    organization_name = models.CharField(max_length=150,
                                         primary_key=True)
    type_study_organization = models.CharField(max_length=3,
                                               choices=STATUS_CHOICES,
                                               default=ORGANIZATION_SH)


class Specialisation(models.Model):
    specialisation_name = models.CharField(max_length=150,
                                           primary_key=True)
    study_time = models.IntegerField()
    specialisation_study_organization = models.ManyToManyField(StudyOrganization,
                                                               blank=True)


class Person(models.Model):
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)
    bio = models.TextField(blank=True)
    specialisation = models.ManyToManyField(Specialisation, blank=True)

    class Meta:
        abstract = True


class Author(Person):
    STATUS_BH = "B"
    STATUS_MH = "M"
    STATUS_PHD = "PHD"

    STATUS_CHOICES = [
        (STATUS_BH, "Bachelor"),
        (STATUS_MH, "Master"),
        (STATUS_PHD, "PhD"),
    ]

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=STATUS_MH)
    study_organizations = models.ManyToManyField(StudyOrganization, blank=True)

    def __str__(self):
        return f" Author <{self.user}>"


class Article(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True,
                                        blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article(title={self.title!r}, author={self.author}"


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True)
    specialisation = models.ForeignKey(Specialisation, blank=False, on_delete=models.CASCADE)
    study_organizations = models.ManyToManyField(StudyOrganization, blank=False)


class Student(Person):
    study_organization = models.ForeignKey(StudyOrganization, blank=True, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, blank=True)


#TODO: Как сделать расписание занятий ?
#TODO: Заполнить базу тестовыми или реальными данными (попробывать написать под это все pytest)
