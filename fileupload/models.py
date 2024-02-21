from django.db import models

# Create your models here.

class fileupload(models.Model):
    file_name = models.FileField(upload_to='videos/')
    file_from = models.CharField(max_length=255)
    camera_number = models.IntegerField()
    video_record_time = models.DateTimeField()
    video_upload_time = models.DateTimeField(auto_now_add=True)
