# from django.test import TestCase 
# from .models import Course

# class TestViews(TestCase):

#     def view_home(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'content/home.html')


#     def CourseListView(self):
#         course = Course.objects.create(name='test course')
#         response = self.client.get('/content')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'content/course_list.html')

    
#     def CourseDetailView(self):
#         response = self.client.get('/content')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'content/course_detail.html')


    
#     def VideoDetailView(self):
#         response = self.client.get('/content')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'content/video_detail.html')

    
    
    


