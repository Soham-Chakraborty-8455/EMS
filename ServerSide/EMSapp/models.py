from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    institution = models.TextField()
    issue_date = models.DateField()

    def __str__(self):
        return self.headline
