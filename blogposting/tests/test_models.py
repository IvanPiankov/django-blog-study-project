import pytest

from blogposting.models import (Specialisation, StudyOrganization, Author, Article, Course, Student)
from django.contrib.auth.models import User


@pytest.fixture
def create_study_organization():
    study_organization = StudyOrganization(organization_name="Test_1", type_study_organization="C")
    study_organization.save()
    return study_organization


@pytest.fixture
def create_specialisation():
    specialisation = Specialisation(specialisation_name="Test_1", study_time=10)
    specialisation.save()
    return specialisation


@pytest.fixture
def create_user():
    u = User(username="user_1", password="user_1")
    u.save()
    return u


@pytest.fixture
def create_author(create_user):
    author = Author(user=create_user, status="PHD")
    author.save()
    return author


@pytest.fixture
def create_article(create_author):
    article = Article(author=create_author, title="test_text")
    article.save()
    return article


@pytest.fixture
def create_course(create_specialisation):
    course = Course(course_name="test_course_name", specialisation=create_specialisation)
    course.save()
    return course


@pytest.fixture
def create_student(create_user, create_study_organization):
    student = Student(user=create_user, study_organization=create_study_organization)
    student.save()
    return student


@pytest.mark.django_db
def test_zero_study_organization_in_db():
    assert StudyOrganization.objects.count() == 0


@pytest.mark.django_db
def test_one_study_organization_in_db(create_study_organization):
    assert StudyOrganization.objects.count() == 1


@pytest.mark.django_db
def test_zero_specialisation_in_db():
    assert Specialisation.objects.count() == 0


@pytest.mark.django_db
def test_one_specialisation_in_db(create_specialisation):
    assert Specialisation.objects.count() == 1


@pytest.mark.django_db
def test_zero_specialisation_and_study_organizations_in_db(create_study_organization, create_specialisation):
    assert len(create_specialisation.specialisation_study_organization.all()) == 0


@pytest.mark.django_db
def test_one_specialisation_and_study_organizations_in_db(create_study_organization, create_specialisation):
    create_specialisation.specialisation_study_organization.add(create_study_organization)
    assert len(create_specialisation.specialisation_study_organization.all()) == 1


@pytest.mark.django_db
def test_zero_author_in_db():
    assert Author.objects.count() == 0


@pytest.mark.django_db
def test_one_author_in_db(create_author):
    assert Author.objects.count() == 1


@pytest.mark.django_db
def test_zero_article_in_db():
    assert Article.objects.count() == 0


@pytest.mark.django_db
def test_one_article_in_db(create_article):
    assert Article.objects.count() == 1


@pytest.mark.django_db
def test_zero_course_in_db():
    assert Course.objects.count() == 0


@pytest.mark.django_db
def test_one_course_in_db(create_course):
    assert Course.objects.count() == 1


@pytest.mark.django_db
def test_zero_student_in_db():
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_one_student_in_db(create_student):
    assert Student.objects.count() == 1