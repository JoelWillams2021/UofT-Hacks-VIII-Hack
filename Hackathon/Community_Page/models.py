from django.db import models

class Community(models.Model):
    community_name = models.CharField(max_length=100)
    community_description = models.CharField(max_length=1000)
    users = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.community_name
