from django.urls import path, include
import blogposting.views as blogposting
from djangoblogproject.settings import DEBUG

app_name = "blogposting"

urlpatterns = [
    path('courses/',
         blogposting.Courses.as_view(template_name='blogposting/courses_list.html'),
         name='courses_list'),
    path('course/<int:pk>/',
         blogposting.ReadCourse.as_view(template_name='blogposting/course.html'),
         name='course_detail'),
    path('course/create/',
         blogposting.CourseCreateView.as_view(template_name='blogposting/create_course.html'),
         name='create_course'),
    path('course/<int:pk>/edit/',
         blogposting.CourseUpdateView.as_view(template_name='blogposting/update_course.html'),
         name='update_course'),
    path('course/<int:pk>/delete/',
         blogposting.CourseDeleteView.as_view(template_name='blogposting/delete_course.html'),
         name='delete_course')
]
