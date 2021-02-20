from django.shortcuts import render, get_object_or_404
from .models import Topic, Subtopic


# Create your views here.
def topic_list_view(request):
    topic_list = Topic.objects.order_by("pub_date")
    return render(request, 'forum/topic_list.html', {"topic_list": topic_list})


def topic_view(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    subtopics = topic.subtopic_set.all()
    return render(request, 'forum.topic_view.html', {"topic": topic,
                                                     "subtopics": subtopics})
