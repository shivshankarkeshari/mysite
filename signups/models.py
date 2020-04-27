from django.db import models


# Create your models here.
class userdb(models.Model):
    email_id = models.EmailField(max_length=80, unique=True)
    First_Name = models.CharField(max_length=80)
    Last_Name = models.CharField(max_length=80)

    def __str__(self):
        return self.First_Name + " " +self.Last_Name