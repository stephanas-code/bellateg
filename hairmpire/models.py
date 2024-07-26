from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100)
    email     = models.EmailField()
    message     = models.CharField(max_length=300)

    
    class Meta:
            verbose_name_plural = "Contacting Us"