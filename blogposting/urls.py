from django.urls import path
import blogposting.views as blogposting

app_name = "blogposting"

urlpatterns = [
    # path('', blogposting.index, name='index'),
    path('courses/', blogposting.Courses.as_view(template_name='blogposting/courses_list.html'), name='courses_list'),
    path('course/<int:pk>/', blogposting.ReadCourse.as_view(template_name='blogposting/course.html'),
         name='course_detail'),
    path('course/create/',
         blogposting.CourseCreateView.as_view(template_name='blogposting/create_course.html'),
         name='create_course')
]
