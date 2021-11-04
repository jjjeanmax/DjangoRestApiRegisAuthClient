from django.db import models
from django.contrib.auth.models import AbstractUser, User
import uuid
from django.utils.safestring import mark_safe


class Client(AbstractUser, models.Model):
    photo = models.ImageField(verbose_name='Photo', upload_to='static/client_api/images/', null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=128, unique=True, default=uuid.uuid1)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    def get_photo(self):
        if not self.photo:
            return '/static/client_api/images/avatar.jpg'  # по умолчанию
        return self.photo.url

    # for create a fictive bd to save img
    def photo_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_photo())

    photo_tag.short_description = 'Photo'
