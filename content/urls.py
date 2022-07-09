from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
# from .views import CategoryDetailView

# as_view from django documented
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    # path('', CategoryDetailView.as_view(), name='category-list'),
    path('<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/learn/<slug>', VideoDetailView.as_view(), name='video-detail')
]