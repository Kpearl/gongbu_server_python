from django.db import models

class Users(models.Model):
    class Meta:
        db_table = 'users'

    email = models.EmailField()
    password = models.TextField()
    nickname = models.TextField()
    phone = models.IntegerField()
    birth = models.DateTimeField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

