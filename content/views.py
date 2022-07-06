from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Video
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CoursePermissionMixin


class CourseListView(ListView):
    """ This class iherit the listView class which means it will have built in features to return a list of objects of a model. """
    # Assign it the Course class to the model variable, because the course 
    # list view inherits from the listView so it will be automaticly 
    # return the list of course objects.(to an array call object_list by default)
    model = Course
    template_name = "content/course_list.html"

    # query to tell the class CourseListView which data need to return, but updating the model variable is more concise, assign it the Course class  to it
    # queryset = Course.objects.all()

class CourseDetailView(DetailView):
    model = Course
    template_name = "content/course_detail.html"

# I used LoginRequiredMixin here so when students try to acces for a Course
# That required a subscription payment will redirect the user to the Login view.
class VideoDetailView(LoginRequiredMixin, CoursePermissionMixin, DetailView):
    model = Video
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs["course_slug"])
        context['course'] = course

        return context

# def display_video(request):
#     videos = Video.objets.all
#     context = {'videos': videos}
#     return render(request, "content/video_detail.html", context)
