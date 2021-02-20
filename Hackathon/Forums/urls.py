from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_forums_view, name='forums'),
    path('<int:topic_id>', views.render_topic_view, name='topic_view'),
]
