from django.urls import path
from .views import CourseDetailView, VideoDetailView, course_list
# from .views import intermediate_course_list, begginers_course_list, teachers_course_list
from . import views
from .views import CategoryDetailView

# as_view from django documented
urlpatterns = [
    path('', views.view_home, name='view_home'),
    path('course/', course_list, name='course-list'),
    # path('category/yoga-teachers/', teachers_course_list, name='teachers'),
    # path('category/begginers/', begginers_course_list, name='begginers'),
    # path('category/intermediate/',  intermediate_course_list, name='intermediate'),
    # path('category/', category_course_list, name='category-course-list'),
    path('<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/learn/<slug>', VideoDetailView.as_view(), name='video-detail')
]