# Generated by Django 4.2 on 2023-05-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]