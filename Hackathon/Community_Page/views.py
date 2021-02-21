from django.shortcuts import render
from .models import Community
# Create your views here.


def render_community_page(request):
    community_list = Community.objects.order_by("pub_date")
    Uoft = Community.objects.order_by("pub_date")[0]
    HDSB = Community.objects.order_by("pub_date")[1]
    return render(request, 'Community_Page/join_a_community_page.html', {"community_list": community_list,
                                                                         "Uoft": Uoft,
                                                                         "HDSB": HDSB})


