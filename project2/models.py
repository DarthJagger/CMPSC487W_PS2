from django.db import models

# Create your models here.


class storeItem(models.Model):
    title = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

