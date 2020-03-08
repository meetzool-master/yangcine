from django.db import models
from core import models as core_models

# Create your models here.
    
class Source(core_models.TimeStampedModel):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    
    script = models.TextField()
    review = models.TextField(max_length=24, help_text="24글자")
    
    source = models.ManyToManyField(Source, blank=True)
    pub_date = models.DateField()
    
    video_url_1 = models.URLField(max_length=300, help_text="예고편")
    video_url_2 = models.URLField(max_length=300, help_text="인터뷰")
    video_url_3 = models.URLField(max_length=300, help_text="OST")
    video_url_4 = models.URLField(max_length=300, help_text="소개영상")
    
    netflix_url = models.URLField(max_length=300, blank=True, null=True)
    watcha_url = models.URLField(max_length=300, blank=True, null=True)
    google_play_url = models.URLField(max_length=300, blank=True, null=True)
    wavve_url = models.URLField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
    