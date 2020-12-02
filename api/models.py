from django.db import models

class Demo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)