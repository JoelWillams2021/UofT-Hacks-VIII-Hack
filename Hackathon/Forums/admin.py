from django.contrib import admin
from .models import Topic, Subtopic, Suggestion, Comment
# Register your models here.
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Suggestion)
admin.site.register(Comment)
