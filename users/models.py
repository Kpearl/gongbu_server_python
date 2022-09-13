from django.db import models


class User(models.Model):
    id = models.AutoField()
    email = models.EmailField()
    password = models.TextField()
    nickname = models.TextField()
    phone = models.IntegerField()
    birth = models.DateTimeField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

