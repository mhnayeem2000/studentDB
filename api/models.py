from django.db import models

# Create your models here.

class Student(models.Model):
    stuID = models.CharField( max_length=50)
    stuName = models.CharField(max_length=50)
    stuDep = models.CharField(max_length=50)
    stuImg = models.ImageField(null=True, blank=True, upload_to="profile_pic/")

    def __str__ (self):
        return self.stuName
    