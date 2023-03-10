from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField()
    # add thumbnail
    # add author

    def __str__(self) -> str:
        return self.title
