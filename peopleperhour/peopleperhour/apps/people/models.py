from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    password = models.CharField(max_length=300)
    is_worker = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


class Worker(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.FloatField()
