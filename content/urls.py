from django.urls import path
from .views import CourseDetailView, VideoDetailView, course_list, intermediate_course_list
from . import views
from .views import CategoryDetailView

# as_view from django documented
urlpatterns = [
    path('', views.view_home, name='view_home'),
    path('course/', course_list, name='course-list'),
    # path('category/yoga-teachers', category_course_list.as_view(), name='category-course-list'),
    # path('category/begginers', category_course_list.as_view(), name='category-course-list'),
    path('category/intermediate/',  intermediate_course_list, name='intermediate'),
    # path('category/midfullness', category_course_list.as_view(), name='category-course-list'),
    path('<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/learn/<slug>', VideoDetailView.as_view(), name='video-detail')
]