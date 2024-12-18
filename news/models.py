from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class News(models.Model):
    author_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    short_content = models.TextField()
    long_content = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'News'

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])
