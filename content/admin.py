from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Course, Section, Video, Category


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Section)

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass


admin.site.register(Video, VideoAdmin)

