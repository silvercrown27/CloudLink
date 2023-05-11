from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

import uuid

class User(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=30, unique=True, verbose_name='Username', validators=[RegexValidator(
        regex='^[a-zA-Z0-9._-]+$',
        message='Username can only contain letters, numbers, periods, underscores, and hyphens.'
    )])
    first_name = models.CharField(max_length=100, verbose_name='firstname')
    last_name = models.CharField(max_length=100, verbose_name='lastname')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=100, verbose_name='Email Address')
    address1 = models.CharField(max_length=100, blank=True, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=10, verbose_name='State')
    zip_code = models.CharField(max_length=10, verbose_name='zip', validators=[RegexValidator(
        regex='^\d{5}(?:[-\s]\d{4})?$',
        message='Zip code must be in the format XXXXX or XXXXX-XXXX.'
    )])
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True, editable=True)
    is_staff = models.BooleanField(default=False)
    allocated_space = models.IntegerField(default=50000, blank=False)
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)], verbose_name='Password')

    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'phone', 'address1', 'city', 'state', 'zip', 'password']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4().hex[:15]).upper()
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def get_short_name(self):
        return self.firstname

    def __str__(self):
        return self.username