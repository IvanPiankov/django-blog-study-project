# TODO: Create serilalizer
# for many to many (many=True)
from rest_framework import routers
from blogposting.api_views import CourseViewSet

app_router = routers.DefaultRouter()
app_router.register(r'restcourse', CourseViewSet)
