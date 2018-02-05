from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'category/static/category')

    def __str__(self):
        return self.name

class Test(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)