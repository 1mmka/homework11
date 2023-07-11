from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    status = models.BooleanField(blank=False,default=False)

    def get_absolute_url(self):
        return f"complete/{self.pk}"

    def __str__(self):
        return self.title