from django.shortcuts import render, redirect
# Create your views here.
def render_home_page(request):
    return render(request, 'Home_Page/Home_Page.html')

def School(request):
    response = redirect('/School')
    return response