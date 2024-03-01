from django.db import models

class Course(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=50)
    Rate = models.IntegerField(default=0)
    Count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Title} - Rate: {self.Rate}"# - Description: {self.Description}, - Count: {self.Count}"
