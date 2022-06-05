from django.db import models
from users.models import *
from django.db.models.signals import post_save
from .signals import post_save_activities_for_language_save

class ServiceLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=100)
    '''video_url = models.URLField(null=True, blank=True)
    video_thumnail = models.ImageField(upload_to='media/thumbnails', null=True, blank=True)'''
    description = models.TextField(null=True, blank=True)
    video_embed_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    categories = models.ForeignKey(DoctorCategory, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    contents = models.ManyToManyField(Content, db_index=True)
    language = models.ForeignKey(ServiceLanguage, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)

    def __str__(self):
        return f'{self.categories.name} ({self.language.name})'
    __str__.short_description = 'Service Name'

    @property
    def service_contents(self):
        return ', '.join(self.contents.all().values_list('title', flat=True))

    @property
    def category(self): return self.categories.name

    @property
    def selected_language(self): return self.language.name


post_save.connect(post_save_activities_for_language_save, sender=ServiceLanguage)