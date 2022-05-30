from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.full_name)
