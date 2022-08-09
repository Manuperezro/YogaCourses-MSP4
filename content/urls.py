from django.urls import path
from .views import CourseDetailView, VideoDetailView, course_list
from . import views
from .views import CategoryDetailView

# as_view from django documented
urlpatterns = [
    path('', views.view_home, name='view_home'),
    path('course/', course_list, name='course-list'),
    path('<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/learn/<slug>', VideoDetailView.as_view(), name='video-detail')
]