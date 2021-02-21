from django.db import models


class Community(models.Model):
    community_name = models.CharField(max_length=100)
    community_description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.community_name


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    topic_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.topic_name


class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subtopic_name


class Suggestion(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    suggestion_text = models.CharField(max_length=255)
    vote_agree = models.IntegerField(default=0)
    vote_unsure = models.IntegerField(default=0)
    vote_disagree = models.IntegerField(default=0)

    def __str__(self):
        return self.suggestion_text


class Comment(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    vote_agree = models.IntegerField(default=0)
    vote_unsure = models.IntegerField(default=0)
    vote_disagree = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
