from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    title = models.CharField('Name', max_length=50)
    full_text = models.TextField('Review')
    date = models.DateField('Date of publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/forum/{self.id}"

    class Meta:
        verbose_name = 'Forum'
        verbose_name_plural = 'Site Forum'


class ForumComment(models.Model):
    full_text = models.TextField('FullText', blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cut = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_text