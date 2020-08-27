# Generated by Django 3.0.8 on 2020-08-27 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_gallery_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead0',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head0',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head1',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='time',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_heading',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blogpost',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='gallery',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
