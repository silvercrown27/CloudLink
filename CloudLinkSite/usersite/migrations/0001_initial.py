# Generated by Django 4.2 on 2023-05-06 22:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drives',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('drive_name', models.CharField(max_length=25)),
                ('capacity', models.IntegerField()),
                ('drive_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=200, verbose_name='Bio')),
                ('links1', models.CharField(blank=True, max_length=100)),
                ('links2', models.CharField(blank=True, max_length=100)),
                ('links3', models.CharField(blank=True, max_length=100)),
                ('links4', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='mainsite.user')),
            ],
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator(message='Path must start with a slash, and can contain letters, digits,hyphens, underscores, dots, at signs, plus signs, and slashes.', regex='^[/\\w.@+-]*(?:[/\\w@+-]+)*$')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('drive_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersite.drives')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator(message='Path must start with a slash, and can contain letters, digits,hyphens, underscores, dots, at signs, plus signs, and slashes.', regex='^[/\\w.@+-]*(?:[/\\w@+-]+)*$')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(max_length=100)),
                ('file_size', models.IntegerField()),
                ('folder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersite.folders')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.user')),
            ],
        ),
    ]
