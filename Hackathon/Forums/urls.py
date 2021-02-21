from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_community_page, name='forums'),
    path('<int:community_id>', views.render_forums_view, name='forums'),
    path('<int:community_id>/<int:topic_id>', views.render_topic_view, name='topic_view'),
]
