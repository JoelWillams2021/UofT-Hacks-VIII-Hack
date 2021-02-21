from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Topic, Subtopic
from .forms import TopicForm


# Create your views here.
def render_forums_view(request):
    topic_list = Topic.objects.order_by("pub_date")
    if request.method == "POST":
        form = TopicForm(request.post)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.save()
            return HttpResponseRedirect("/")
    else:
        form = TopicForm()
    return render(request, 'Forums/forums.html', {"topic_list": topic_list,
                                                  'form': form})


def render_topic_view(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    subtopics = topic.subtopic_set.all()
    suggestions_dict = {}
    for subtopic in subtopics:
        suggestions_dict[subtopic] = subtopic.suggestion_set.all()
    return render(request, 'Forums/topic_view.html', {"topic": topic,
                                                      "subtopics": subtopics,
                                                      "suggestions_dict": suggestions_dict})


def render_subtopic_view(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, pk=subtopic_id)
    suggestions = subtopic.suggestion_set.all()
