from django.urls import path
import blogposting.views as blogposting

app_name = "blogposting"

urlpatterns = [
    path('', blogposting.index, name='index'),
    path('courses/', blogposting.courses_list, name='courses_list'),
    path('course/<int:pk>/', blogposting.course, name='course'),

]
