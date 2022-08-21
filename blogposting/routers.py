
# for many to many (many=True)
from rest_framework import routers
from blogposting.api_views import CourseViewSet, AuthorViewSet

app_router = routers.DefaultRouter()
app_router.register(r'api-course', CourseViewSet)
app_router.register(r'api-author', AuthorViewSet)
