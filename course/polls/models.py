from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    rate = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - Rate: {self.rate}- Description: {self.Description}, - Count: {self.Count}"
    
    
