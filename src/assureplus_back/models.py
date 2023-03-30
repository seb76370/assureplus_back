from django.db import models

class Users(models.Model):

    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contract_number = models.IntegerField(unique=True)

class Sinitres(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sinitre',null = True)
    description = models.TextField()

class Comments(models.Model):
    sinitre = models.ForeignKey(Sinitres, on_delete=models.CASCADE, related_name='comment',null = True)
    comment = models.CharField(max_length=255)
    date = models.DateField()

class files_upload(models.Model):
    sinitre = models.ForeignKey(Sinitres, on_delete=models.CASCADE, related_name='files_upload',null = True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
