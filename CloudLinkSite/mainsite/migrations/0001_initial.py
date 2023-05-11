# Generated by Django 4.2 on 2023-05-07 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Username can only contain letters, numbers, periods, underscores, and hyphens.', regex='^[a-zA-Z0-9._-]+$')], verbose_name='Username')),
                ('first_name', models.CharField(max_length=100, verbose_name='firstname')),
                ('last_name', models.CharField(max_length=100, verbose_name='lastname')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email Address')),
                ('address1', models.CharField(blank=True, max_length=100, verbose_name='Address Line 1')),
                ('address2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=10, verbose_name='State')),
                ('zip_code', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Zip code must be in the format XXXXX or XXXXX-XXXX.', regex='^\\d{5}(?:[-\\s]\\d{4})?$')], verbose_name='zip')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('allocated_space', models.IntegerField(default=50000)),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Password')),
            ],
        ),
    ]
