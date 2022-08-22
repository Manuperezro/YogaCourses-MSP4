from django.test import TestCase 
from .models import Course, Video, Section
from django.contrib.auth import get_user_model

class TestViews(TestCase):


    def setUp(self):
        # setup before the tests
        course = Course.objects.create(name='test course', slug='test-course')
        section = Section.objects.create(title='test section', position=1, course=course)
        video = Video.objects.create(title='test video 1', video_url='google.fr', position=1, section=section, slug='test-video-1', thumbnail='/xxx')
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_view_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/home.html')


    def test_course_list_view(self):
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/course_list.html')

    
    def test_course_detail_view(self):
        course = Course.objects.all().first()
        response = self.client.get(course.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/course_detail.html')

    
    def test_video_detail_view(self):
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')
        video = Video.objects.all().first()
        response = self.client.get(video.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/video_detail.html')

