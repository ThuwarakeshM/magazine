from django.db import models
from markdownx.models import MarkdownxField 

class Tag(models.Model):
    name=models.CharField(max_length=20)
    uri=models.CharField(max_length=20, editable=False, primary_key=True)

    def save(self, *args, **kwargs):
       self.uri = self.name.replace(' ', '_').lower()
       super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


# Create your models here.
class Blog(models.Model):
    uri = models.CharField(max_length=50, primary_key=True)

    # Blog Meta Data
    pub_date = models.DateField()
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    
    # Blog Content
    content = MarkdownxField()

    def save(self, *args, **kwargs):
       self.uri = self.uri.replace(' ', '_').lower()
       super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-pub_date']

