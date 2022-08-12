from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)