from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
from . import views
# from .views import CategoryDetailView

# as_view from django documented
urlpatterns = [
    path('', views.view_home, name='view_home'),
    path('course/', CourseListView.as_view(), name='course-list'),
    # path('category/', CategoryDetailView.as_view(), name='category-list'),
    path('<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/learn/<slug>', VideoDetailView.as_view(), name='video-detail')
]