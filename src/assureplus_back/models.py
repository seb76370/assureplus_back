from datetime import datetime
from django.db import models
from user_api.models import Users

class Sinistres(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sinistre',null = True)
    description = models.TextField()
    cloture = models.BooleanField(default=False)
    date_time = models.DateTimeField(default=datetime.now,)

class Comments(models.Model):
    sinistre = models.ForeignKey(Sinistres, on_delete=models.CASCADE, related_name='comment',null = True)
    comment = models.CharField(max_length=255)
    date_time = models.DateTimeField(default=datetime.now,)

class files_upload(models.Model):
    def __str__(self):
        return f"./{str(self.file)}"
    
    sinistre = models.ForeignKey(Sinistres, on_delete=models.CASCADE, related_name='files_upload',null = True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date_time = models.DateTimeField(default=datetime.now,)
