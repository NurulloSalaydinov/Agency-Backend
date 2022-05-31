from django.db import models


class Attractions(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='attraction_images')

    def __str__(self):
        return str(self.title)


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.full_name)
