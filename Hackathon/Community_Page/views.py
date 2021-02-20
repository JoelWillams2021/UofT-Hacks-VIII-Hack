from django.shortcuts import render
from .models import Community
# Create your views here.

def render_community_page(request):
    community_list = Community.objects.order_by("pub_date")
    return render(request, 'Community_Page/communitypage.html', {"community_list": community_list})

2
def redirect_forums(request):
    return render(request, 'Community_Page/communitypage.html', {"community_list": community_list})
