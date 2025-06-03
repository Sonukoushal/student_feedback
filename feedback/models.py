from django.db import models

class StudentFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name
