from django.db import models

# Create your models here.


class Reminder(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(default="")
    isDone = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.title
    