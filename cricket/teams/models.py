from django.db import models

# Create your models here.
class teams(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    class Meta:
        db_table="teams"
    def __str__(self):
        return self.name
