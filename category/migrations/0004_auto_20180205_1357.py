# Generated by Django 2.0.2 on 2018-02-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20180205_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='static/category/default.png', upload_to='static/category'),
        ),
    ]
