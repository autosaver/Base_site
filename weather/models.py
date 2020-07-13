from django.db import models


# Create your models here.
class weather_searches(models.Model):
    text = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'Weather-Searches'
