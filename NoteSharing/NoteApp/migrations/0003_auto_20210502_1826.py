# Generated by Django 3.0 on 2021-05-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteApp', '0002_auto_20210501_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_avail',
            name='Book_author',
            field=models.CharField(default='', max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='books_avail',
            name='Book_name',
            field=models.CharField(max_length=120),
        ),
    ]
