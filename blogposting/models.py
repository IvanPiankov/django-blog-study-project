from django.contrib.auth import get_user_model
from django.db import models


class StudyOrganization(models.Model):
    pass

class Specialisation(models.Model):
    pass

class Author(models.Model):
    # lite variant we can do chooses object with chooses object in Django documentations
    STATUS_BH = "B"
    STATUS_MH = "M"
    STATUS_PHD = "PHD"

    STATUS_CHOICES = [
        (STATUS_BH, "Bachelor"),
        (STATUS_MH, "Master"),
        (STATUS_PHD, "PhD"),
    ]
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=STATUS_MH)

    bio = models.TextField(blank=True)

    study_organizations = models.ManyToManyField(StudyOrganization,
                                                 max_length=200,
                                                 default="",
                                                 blank=True)
    specialisation = models.ManyToManyField(Specialisation,
                                            max_length=200,
                                            default="",
                                            blank=True)

    def __str__(self):
        return f" Author <{self.user}>"


