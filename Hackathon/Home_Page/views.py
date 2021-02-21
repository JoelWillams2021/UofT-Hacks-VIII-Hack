from django.shortcuts import render, redirect

# Create your views here.
def render_home_page(request):
    return render(request, 'Home_Page/homepage.html')

def render_cp(request):
    return render(request, 'Home_Page/join_a_community_page.html')