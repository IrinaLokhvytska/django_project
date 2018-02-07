# Generated by Django 2.0.2 on 2018-02-07 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0012_auto_20180207_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Test', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category', verbose_name='Category'),
        ),
    ]