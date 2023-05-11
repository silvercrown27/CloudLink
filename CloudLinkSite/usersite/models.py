from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

from mainsite.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
    bio = models.CharField(max_length=200, blank=True, verbose_name='Bio')
    links1 = models.CharField(max_length=100, blank=True)
    links2 = models.CharField(max_length=100, blank=True)
    links3 = models.CharField(max_length=100, blank=True)
    links4 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username + "'s Profile"


class Drives(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True, blank=False, null=False)
    drive_name = models.CharField(max_length=25, null=False, blank=False, editable=True)
    drive_user = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4().hex[:15]).upper()
        super().save(*args, **kwargs)


class Folders(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    path_regex = RegexValidator(
        regex=r'^[/\w.@+-]*(?:[/\w@+-]+)*$',
        message='Path must start with a slash, and can contain letters, digits,'
                'hyphens, underscores, dots, at signs, plus signs, and slashes.')
    path = models.CharField(validators=[path_regex], max_length=1000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now_add=True)
    drive_id = models.ForeignKey(Drives, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4().hex[:15]).upper()
        super().save(*args, **kwargs)


class Files(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    path_regex = RegexValidator(
        regex=r'^[/\w.@+-]*(?:[/\w@+-]+)*$',
        message='Path must start with a slash, and can contain letters, digits,'
                'hyphens, underscores, dots, at signs, plus signs, and slashes.')
    path = models.CharField(validators=[path_regex], max_length=1000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    file_ext = models.CharField(max_length=100, blank=True)
    file_size = models.IntegerField(blank=True, null=True)
    folder_id = models.ForeignKey(Folders, on_delete=models.CASCADE)
    drive_id = models.ForeignKey(Drives, on_delete=models.CASCADE, default=1)

    def clean(self):
        max_file_size = self.drive_id.capacity
        if self.file_size and self.file_size > max_file_size:
            raise ValidationError(f'The file size ({self.file_size}) exceeds the maximum capacity of the drive ({max_file_size}).')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4().hex[:15]).upper()
        super().save(*args, **kwargs)