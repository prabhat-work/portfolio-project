from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=10)
    pub_date=models.DateTimeField()
    body=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
