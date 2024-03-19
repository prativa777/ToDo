from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    detail = models.CharField(max_length=256)

    def __str__(self):
        return self.title