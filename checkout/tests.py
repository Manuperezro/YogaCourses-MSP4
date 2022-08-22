from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Course

# Create your tests here.

class TestCheckout(TestCase):


    def setUp(self):
        # setup before the tests
        self.course = Course.objects.create(name='test course', slug='test-course')
        User = get_user_model()
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
    
    def test_view_checkout(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)