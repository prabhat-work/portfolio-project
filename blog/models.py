from django.db import models

class blog(models.Model):
    title=models.TextField(max_length=1000)
    pub_date=models.DateTimeField()
    body=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images/')

def __str__(self):
    return self.title
