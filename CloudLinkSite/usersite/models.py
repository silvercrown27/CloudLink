import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# create a new FileSystemStorage instance
fs = FileSystemStorage()

class Folder(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class File(models.Model):
    FILE_TYPES = (
        ('V', 'Video'),
        ('P', 'Picture'),
        ('M', 'Music'),
        ('D', 'Document'),
    )

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_type = models.CharField(max_length=1, choices=FILE_TYPES)
    created_at = models.DateTimeField(default=timezone.now)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def create_from_upload(cls, uploaded_file, folder_id):
        """
        Create a new File instance from an uploaded file.
        """
        # get the original filename and extension
        file_name, file_ext = os.path.splitext(uploaded_file.name)

        # get the file type based on the extension
        file_type = None
        for file_type_choice in cls.FILE_TYPES:
            if file_ext.lower() in FILE_TYPE_CHOICES[file_type_choice[0]]:
                file_type = file_type_choice[0]
                break

        if not file_type:
            # if the file type is not recognized, don't create the file
            return None

        # save the file to the default storage
        file_path = fs.save(uploaded_file.name, uploaded_file)

        # create a new File instance and save it to the database
        new_file = cls(
            name=uploaded_file.name,
            file=file_path,
            file_type=file_type,
            folder_id=folder_id
        )
        new_file.save()

        return new_file