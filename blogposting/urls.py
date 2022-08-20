from django.urls import path, include
import blogposting.views as blogposting
from blogposting.routers import app_router
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
         name='delete_course'),
    path('authors/',
         blogposting.AuthorsList.as_view(template_name='blogposting/authors_list.html'),
         name='authors_list'),
    path('author/<int:pk>/',
         blogposting.AuthorDetail.as_view(template_name='blogposting/author_detail.html'),
         name='author_detail'),
    path('author/create/',
         blogposting.CreateAuthor.as_view(template_name='blogposting/create_author.html'),
         name='create_author'),
    path('feedback/', blogposting.SendEmail.as_view(template_name='blogposting/feedback.html'),
         name='feedback')

    path('', include(app_router.urls)),
]
