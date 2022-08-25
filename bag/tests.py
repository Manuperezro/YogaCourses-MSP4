from django.test import TestCase
from content.models import Course
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.

class TestBag(TestCase):

    @classmethod
    def setUp(self):
        # setup before the tests
        self.course = Course.objects.create(name='test course', slug='test-course', price='2')
        User = get_user_model()
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_add_to_bag(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.post('/bag/add/'+str(self.course.id), data={'quantity':'1', 'redirect_url':'/'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('view_bag'))
        self.assertContains(response, "test course")
        self.assertTemplateUsed(response, "bag/bag.html")
        self.assertEqual(response.status_code, 200)
