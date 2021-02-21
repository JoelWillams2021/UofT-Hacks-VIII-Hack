from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Topic, Subtopic, Community
from .forms import TopicForm


def render_community_page(request):
    community_list = Community.objects.order_by("pub_date")
    Uoft = Community.objects.order_by("pub_date")[0]
    HDSB = Community.objects.order_by("pub_date")[1]
    return render(request, 'Forums/join_a_community_page.html', {"community_list": community_list,
                                                                         "Uoft": Uoft,
                                                                         "HDSB": HDSB})


def render_forums_view(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    topic_list = community.topic_set.all()
    return render(request, 'Forums/forums.html', {"community": community,
                                                  "topic_list": topic_list})


def render_topic_view(request, community_id, topic_id):
    community = get_object_or_404(Community, pk=community_id)
    topic = get_object_or_404(Topic, pk=topic_id)
    subtopics = topic.subtopic_set.all()
    return render(request, 'Forums/topic_view.html', {"community": community,
                                                      "topic": topic,
                                                      "subtopics": subtopics})


def render_subtopic_view(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, pk=subtopic_id)
    suggestions = subtopic.suggestion_set.all()
    comments = subtopic.comment_set.all()
    return render(request, 'Forums/topic_view.html', {"subtopic": subtopic,
                                                      "suggestions": suggestions,
                                                      "comments": comments})
