# Generated by Django 2.0.2 on 2018-02-06 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20180205_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]