from django.db import models

# Create your models here.
class store(models.Model):
    fname=models.CharField(max_length=20)
    fpass=models.CharField(max_length=20)


    def __str__(self):
        return f"{self.fname}"