from django.contrib import admin

from blogposting.models import (Specialisation, StudyOrganization, Author, Article, Course, Student)

admin.site.register(Author)
admin.site.register(Specialisation)
admin.site.register(StudyOrganization)
admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Student)
