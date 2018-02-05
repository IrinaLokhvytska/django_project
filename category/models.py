from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'static/category', default = 'static/category/default.png')

    def __str__(self):
        return self.name
