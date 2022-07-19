import pytest

from blogposting.models import Specialisation


@pytest.mark.django_db
def test_create_specialisation():
    specialisation = Specialisation(specialisation_name="Test_1", study_time=10)
    specialisation.save()
    assert Specialisation.objects.count() == 1
