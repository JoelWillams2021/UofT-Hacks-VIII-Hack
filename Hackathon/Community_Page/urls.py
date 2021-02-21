from django.urls import path
from . import views

urlpatterns = [
    path('Communities', views.render_community_page, name='community_page'),
]
