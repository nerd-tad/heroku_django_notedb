from django.db import models

# Create your models here.
class Notes(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[0:50]  #the string representation will be reduced to 50 chars

    class Meta:
        ordering = ['-updated']
