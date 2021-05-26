from django.db import models

# Create your models here.
class SearchQuery(models.Model):
    query_title = models.CharField(max_length=100)

    def __str__(self):
        return self.query_title

class InfoResults(models.Model):
    page_url = models.CharField(max_length=100)

    def __str__(self):
        return "page found at: " + self.page_url