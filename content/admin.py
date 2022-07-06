from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Category, Course, Section, Video

# Register the models of the app 

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Section)
# admin.site.register(Video)

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass


admin.site.register(Video, VideoAdmin)

