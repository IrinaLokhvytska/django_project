from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'category/static/image')

    def __str__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Test")

class Question(models.Model):
    description = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Question")

    def __str__(self):
        return self.description

class Answer(models.Model):
    answer = models.TextField()
    correctness = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Answer")

    def __str__(self):
        return self.answer