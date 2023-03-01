from django.db import models


# Create your models here.
class UserFrom(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"
