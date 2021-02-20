from django.shortcuts import render, get_object_or_404
from .models import Topic, Subtopic


# Create your views here.
def render_forums_view(request):
    topic_list = Topic.objects.order_by("pub_date")
    return render(request, 'Forums/forums.html', {"topic_list": topic_list})


def render_topic_view(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    subtopics = topic.subtopic_set.all()
    return render(request, 'Forums/topic_view.html', {"topic": topic,
                                                      "subtopics": subtopics})


def render_subtopic_view(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, pk=subtopic_id)
    suggestions = subtopic.suggestion_set.all()
