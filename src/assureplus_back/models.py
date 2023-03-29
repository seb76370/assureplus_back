from django.db import models

# class users(models.Model):

#     def __str__(self):
#         return self.name

#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     street = models.CharField(max_length=30)
#     zipcode = models.CharField(max_length=30)
#     city = models.CharField(max_length=30)
#     contract_number = models.IntegerField()

class files_upload(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
