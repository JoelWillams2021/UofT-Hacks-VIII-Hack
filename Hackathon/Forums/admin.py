from django.contrib import admin
from .models import Topic, Subtopic, Suggestion, Comment, Community
# Register your models here.
admin.site.register(Community)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Suggestion)
admin.site.register(Comment)
