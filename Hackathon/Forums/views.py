from django.shortcuts import render

# Create your views here.
def render_forums(request):
    return render(request, 'Forums/forums.html')