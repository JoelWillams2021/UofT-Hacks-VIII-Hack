from django import forms
from .models import Topic, Subtopic, Suggestion, Community


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class SubtopicForm(forms.ModelForm):
    class Meta:
        model = Subtopic
        fields = "__all__"


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ("suggestion_text",)


class VoteForm(forms.Form):
    options = ("AGREE", "NOT SURE", "DISAGREE")
    choice = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
